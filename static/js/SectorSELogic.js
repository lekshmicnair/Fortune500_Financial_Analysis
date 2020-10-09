// Sector URL
var urlSector = "http://127.0.0.1:5000/sector";

d3.json(urlSector, function(SectorData) {

    console.log(SectorData)

    const dataSource = {
        chart: {
            caption: "Fortune500 Companies by Sector",
            showvalues: "1",
            showpercentintooltip: "0",
            showLegend: "0",
            enablemultislicing: "1",
            theme: "fusion",
            plottooltext: "$label, <b>$dataValue</b> Companies",
        },
        data: SectorData[0]
    };
    
    FusionCharts.ready(function() {
      var myChart = new FusionCharts({
        type: "pie3d",
        renderAt: "chart-container",
        width: "100%",
        height: "350%",
        dataFormat: "json",
        dataSource
      }).render();
    });
});

d3.json(urlSector, function(SectorData) {
    const dataSource = {
        chart: {
        caption: "Number of Employees by Sector",
        showvalues: "1",
        showpercentintooltip: "0",
        showLegend: "0",
        enablemultislicing: "1",
        theme: "fusion",
        plottooltext: "$label, <b>$dataValue</b> Employees",
        },
        data: SectorData[1]
    };
    
    FusionCharts.ready(function() {
        var myChart2 = new FusionCharts({
        type: "pie3d",
        renderAt: "chart-container2",
        width: "100%",
        height: "190%",
        dataFormat: "json",
        dataSource
        }).render();
    });
});