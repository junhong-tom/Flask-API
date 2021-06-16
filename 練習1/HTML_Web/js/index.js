function postData(url,data) {
    return fetch(url,{
    body: JSON.stringify(data),
    cache: 'no-cache',
    credentials: 'same-origin',
    headers:{
        'user-agent': 'Example',
        'content-type': 'application/json'
    },
    method:'POST',
    mode:'cors',
    redirect:'follow',
    referrer:'no-referrer'

    }).then(response => response.json()) // 輸出 json
}
function predictType(result){
    if (result > 0.5)
        return '陽性';
    else
        return '陰性';
}

function submit(){
    const Pregnancies = document.getElementById('Pregnancies').value;
    const Glucose = document.getElementById('Glucose').value;
    const BloodPressure = document.getElementById('BloodPressure').value;
    const SkinThickness = document.getElementById('SkinThickness').value;
    const Insulin = document.getElementById('Insulin').value;
    const BMI = document.getElementById('BMI').value;
    const DiabetesPedigreeFunction = document.getElementById('DiabetesPedigreeFunction').value;
    const Age= document.getElementById('Age').value;

    const data = {
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
    }

    postData('http://192.168.0.50:3000/predict',data)
    .then(data => {
        const result = data.result;
        console.log(data);
        console.log(result);
        console.log(predictType(result));
        document.getElementById('resultText').innerHTML = predictType(result);
    })

}
