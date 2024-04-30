import init, { Universe, Cell } from "@/assets/game_of_life/wasm_game_of_life.js";
import PlayArrowIcon from '@/assets/icons/play_arrow.svg'
import PauseIcon from '@/assets/icons/pause.svg'

const wasm = await init()

const CELL_SIZE = 5; // px
const GRID_COLOR = "#CCCCCC";
const DEAD_COLOR = "#FFFFFF";
const ALIVE_COLOR = "#000000";

// Construct the universe, and get its width and height.
const universe = Universe.new();
const width = universe.width();
const height = universe.height();

// Give the canvas room for all of our cells and a 1px border
// around each of them.
const canvas = document.getElementById("game-of-life-canvas");
canvas.height = (CELL_SIZE + 1) * height + 1;
canvas.width = (CELL_SIZE + 1) * width + 1;

const ctx = canvas.getContext('2d');

canvas.addEventListener("click", event => {
  const boundingRect = canvas.getBoundingClientRect();

  const scaleX = canvas.width / boundingRect.width;
  const scaleY = canvas.height / boundingRect.height;

  const canvasLeft = (event.clientX - boundingRect.left) * scaleX;
  const canvasTop = (event.clientY - boundingRect.top) * scaleY;

  const row = Math.min(Math.floor(canvasTop / (CELL_SIZE + 1)), height - 1);
  const col = Math.min(Math.floor(canvasLeft / (CELL_SIZE + 1)), width - 1);

  if (event.shiftKey) {
    universe.set_cell_alive(row, col);
    universe.set_cell_alive(row, col - 1);
    universe.set_cell_alive(row, col - 2);
    universe.set_cell_alive(row - 1, col);
    universe.set_cell_alive(row - 2, col - 1);
  } else if (event.ctrlKey) {
    let pulsar = [
      [1, 2], [1, 3], [1, 4],
      [2, 1], [3, 1], [4, 1],
      [6, 2], [6, 3], [6, 4],
      [2, 6], [3, 6], [4, 6]
    ]

    for (let [op_y, op_x] of [[1, 1], [1, -1], [-1, 1], [-1, -1]]) {
      for (const [y, x] of pulsar) {
        let new_y = (row + y * op_y) % height;
        let new_x = (col + x * op_x) % width;

        if (new_y < 0) new_y += height
        if (new_x < 0) new_x += width
        
        universe.set_cell_alive(new_y, new_x);
      }
    }

  } else {
    universe.toggle_cell(row, col);
  }

  drawGrid();
  drawCells();
});

const fpsControl = document.getElementById("fps-control");

fpsControl.addEventListener("input", (e) => {
  interval = 1000 / +e.target.value;
});

let animationId = null;
let interval = 1000 / +fpsControl.value;
let then;
const renderLoop = (timestamp) => {
  if (then === undefined) {
    then = timestamp;
  }

  const delta = timestamp - then;

  if (delta > interval) {
    then = timestamp - (delta % interval);

    universe.tick();

    drawGrid();
    drawCells();
  }

  animationId = requestAnimationFrame(renderLoop);
};

const drawGrid = () => {
  ctx.beginPath();
  ctx.strokeStyle = GRID_COLOR;

  // Vertical lines.
  for (let i = 0; i <= width; i++) {
    ctx.moveTo(i * (CELL_SIZE + 1) + 1, 0);
    ctx.lineTo(i * (CELL_SIZE + 1) + 1, (CELL_SIZE + 1) * height + 1);
  }

  // Horizontal lines.
  for (let j = 0; j <= height; j++) {
    ctx.moveTo(0, j * (CELL_SIZE + 1) + 1);
    ctx.lineTo((CELL_SIZE + 1) * width + 1, j * (CELL_SIZE + 1) + 1);
  }

  ctx.stroke();
};

const getIndex = (row, column) => {
  return row * width + column;
};

const drawCells = () => {
  const cellsPtr = universe.cells();
  const cells = new Uint8Array(wasm.memory.buffer, cellsPtr, width * height);

  ctx.beginPath();

  // Alive cells.
  ctx.fillStyle = ALIVE_COLOR;
  for (let row = 0; row < height; row++) {
    for (let col = 0; col < width; col++) {
      const idx = getIndex(row, col);
      if (cells[idx] !== Cell.Alive) {
        continue;
      }

      ctx.fillRect(
        col * (CELL_SIZE + 1) + 1,
        row * (CELL_SIZE + 1) + 1,
        CELL_SIZE,
        CELL_SIZE
      );
    }
  }

  // Dead cells.
  ctx.fillStyle = DEAD_COLOR;
  for (let row = 0; row < height; row++) {
    for (let col = 0; col < width; col++) {
      const idx = getIndex(row, col);
      if (cells[idx] !== Cell.Dead) {
        continue;
      }

      ctx.fillRect(
        col * (CELL_SIZE + 1) + 1,
        row * (CELL_SIZE + 1) + 1,
        CELL_SIZE,
        CELL_SIZE
      );
    }
  }

  ctx.stroke();
};

document
  .getElementById("kill-all")
  .addEventListener("click", (e) => {
    universe.clear();
    drawCells();
  });

document
  .getElementById("restart")
  .addEventListener("click", (e) => {
    universe.restart();
    drawCells();
  });

const playPauseButton = document.getElementById("play-pause");

const isPaused = () => {
  return animationId === null;
};

const play = () => {
  playPauseButton.src = PauseIcon;
  renderLoop();
};

const pause = () => {
  playPauseButton.src = PlayArrowIcon;
  cancelAnimationFrame(animationId);
  animationId = null;
};

playPauseButton.addEventListener("click", event => {
  if (isPaused()) {
    play();
  } else {
    pause();
  }
});

drawGrid();
drawCells();
playPauseButton.src = PlayArrowIcon;
