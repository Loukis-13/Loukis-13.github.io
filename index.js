let cor = 1
for (let i of document.getElementsByClassName("bloco")) {
    if (cor) {i.classList.add("darken-2"); cor=0;}
    else {i.classList.add("darken-3"); cor=1;}
}

function change(v) {
    let apis = ["timestamp", "header_parser", "url_shortener", "exercise", "filemetadata"];
    apis.forEach( (x)=>document.getElementById(x).style.display="none" );
    document.getElementById(v).style.display="block";
}
change(document.getElementById("a").value)


const url = "https://1kdj7dtvil.execute-api.us-east-2.amazonaws.com/api";
const heroku = "https://apis-microservices-project.herokuapp.com/api";

function timestamp() {
    time = document.getElementById("data").value;
    window.open(url + "/timestamp/" + time)
}

const exerciseForm = document.getElementById("exercise-form"); 
exerciseForm.addEventListener("submit", () => { 
    const userId = document.getElementById("uid").value;
    exerciseForm.action = `https://apis-microservices-project.herokuapp.com/api/exercise-tracker/users/${userId}/exercises`; 
    exerciseForm.submit(); 
}); 
