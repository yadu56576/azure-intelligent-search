function search(){

let query = document.getElementById("query").value;

fetch("http://localhost:5000/search?q=" + query)
.then(response => response.json())
.then(data => {

let output = "";

data.forEach(doc => {
output += "<h3>"+doc.title+"</h3><p>"+doc.content+"</p>";
});

document.getElementById("results").innerHTML = output;

});

}