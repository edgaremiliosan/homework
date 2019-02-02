// from data.js
var tableData = data;

// YOUR CODE HERE!

var tablebody = d3.select("tbody");

function buildTable(data) {
  tablebody.html("");
  data.forEach((dataRow) => {
  var row = tablebody.append("tr");
  Object.values(dataRow).forEach((val) => {
  var cell = row.append("td");
  cell.text(val); } );  });}

function handleClick() {

  d3.event.preventDefault();

  var date = d3.select("#datetime").property("value");
  let filteredData = tableData;

  if (date) { filteredData = filteredData.filter(row => row.datetime === date);  }

  buildTable(filteredData);}

d3.selectAll("#filter-btn").on("click", handleClick);

buildTable(tableData);
