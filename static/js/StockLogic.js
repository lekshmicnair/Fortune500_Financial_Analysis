// Sector URL
var url = "http://127.0.0.1:5000/api/stock";

d3.json(url).then((importedData) => {
    console.log(importedData);
});

function graphs(id) {

    d3.json(url).then((stockData) => {
        
        var data1 = stockData.LabelPackage[id];
        var data2 = stockData[id];

        console.log(data1)

        const dataSource = {
            chart: {
                caption: `${id} Stock Information`,
                subcaption: "Time Period",
                numberprefix: "$",
                pyaxisname: "Price (USD)",
                theme: "fusion",
                showvolumechart: "1",
                vnumberprefix: "$",
                vyaxisname: "Volume traded"
            },
            categories: [
                {
                  category: data1
                }
              ],
            dataset: [
                {
                data: data2
                }
            ]
            };
            
            FusionCharts.ready(function() {
            var myChart = new FusionCharts({
                type: "candlestick",
                renderAt: "chart-container",
                width: "100%",
                height: "300%",
                dataFormat: "json",
                dataSource
            }).render();
        });
    });
};

// Function for change event
function optionChanged(id) {
    graphs(id);
}

// Initial data rendering
function init() {

    // Select the ID dropdown
    var dataSelect = d3.select("#selDataset");

    // Import data from json file 
    d3.json(url).then((stockData) => {

        // Display IDs in dropdown menu
        stockData.stockName.forEach(function(name) {
            dataSelect.append("option").text(name).property("value");
        });

        // Run graphing and demo panel functions
        graphs(stockData.names);
    });
}

init();