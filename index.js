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
    const userId = document.getElementById("userId").value;
    exerciseForm.action = `https://apis-microservices-project.herokuapp.com/api/exercise-tracker/users/${userId}/exercises`; 
    exerciseForm.submit(); 
}); 

url_dados = {
    'mvs': 'https://colab.research.google.com/drive/1XqWO1akL_v2Rvve8x1E-qQqvRqnI3kxy?usp=sharing',
    'medical_data': 'https://colab.research.google.com/drive/1gabe6Tdy0SfPBIpHG1_FJ0168imXz7h1?usp=sharing',
    'demographic': 'https://colab.research.google.com/drive/1z-AFWAm185-hAy_kAYYNYAuRvFu-9cE_?usp=sharing',
    'page_view': 'https://colab.research.google.com/drive/11qkOfJlo-8JKne7wPtd39xVINqLYS-vJ?usp=sharing',
    'sea_level': 'https://colab.research.google.com/drive/17_eYVYndSfQ5lVeltbytLF2NbBtMluyM?usp=sharing'
}

function open_dados() {
    window.open(url_dados[document.getElementById("opcaoAnaliseDeDados").value])
}
