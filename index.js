 //https://howtocreateapps.com/fetch-and-display-json-html-javascript/
//fetch('http://localhost:4500/TOP?name=PS5&ranking=5')
fetch('http://localhost:5000/get_ps5', {mode: 'cors'})
    .then(function (response) {
        console.log(response)
        return response.json();
    })
    .then(function (data) {
        console.log("my data",data)
        appendPs5(data);

    })
    .catch(function (err) {
        console.log(err);
    });

fetch('http://localhost:5000/get_pc', {mode: 'cors'})
    .then(function (response) {
        console.log(response)
        return response.json();
    })
    .then(function (data1) {
        console.log("my data",data1)
        appendPc(data1);

    })
    .catch(function (err) {
        console.log(err);
    });


fetch('http://localhost:5000/get_xbox', {mode: 'cors'})
    .then(function (response) {
        console.log(response)
        return response.json();
    })
    .then(function (data2) {
        console.log("my data",data2)
        appendXbox(data2);

    })
    .catch(function (err) {
        console.log(err);
    });


    function appendPs5(data){
        var mainContainer = document.getElementById("myData");    
        Object.keys(data).forEach(function(key) {
            console.log('Key : ' + key + ', Value : ' + data[key])
            var div = document.createElement("div");
            div.innerHTML = data[key];
            mainContainer.appendChild(div);
          })
    }

    function appendPc(data1){
        var mainContainer = document.getElementById("myData1");    
        Object.keys(data1).forEach(function(key) {
            console.log('Key : ' + key + ', Value : ' + data1[key])
            var div = document.createElement("div");
            div.innerHTML = data1[key];
            mainContainer.appendChild(div);
          })
    }

    function appendXbox(data2){
        var mainContainer = document.getElementById("myData2");    
        Object.keys(data2).forEach(function(key) {
            console.log('Key : ' + key + ', Value : ' + data2[key])
            var div = document.createElement("div");
            div.innerHTML = data2[key];
            mainContainer.appendChild(div);
          })
    }






// function appendData(data) {
//     var mainContainer = document.getElementById("myData");
//     for (var i = 0; i < data.length; i++) {
//         var div = document.createElement("div");
//         div.innerHTML = data[i];
//         mainContainer.appendChild(div);
//     }

    

// }

