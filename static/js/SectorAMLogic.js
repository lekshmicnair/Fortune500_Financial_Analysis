// Sector URL
var urlSector = "http://127.0.0.1:5000/sector";

d3.json(urlSector, function(SectorData) {

    console.log(SectorData[7])

    const dataSource = {
        chart: {
          caption: "Total Assets by Sector",
          subcaption: "In Millions",
          showpercentvalues: "1",
          showLegend: "0",
          defaultcenterlabel: `Total Assets: $${SectorData[7]} Million`,
          aligncaptionwithcanvas: "0",
          captionpadding: "0",
          decimals: "1",
          plottooltext:
            "<b>$percentValue</b> of Assets owned by <b>$label</b> Sector",
          centerlabel: "$label: $value",
          theme: "fusion"
        },
        data: SectorData[6]
      };
      
      FusionCharts.ready(function() {
        var myChart = new FusionCharts({
          type: "doughnut2d",
          renderAt: "chart-container",
          width: "100%",
          height: "400%",
          dataFormat: "json",
          dataSource
        }).render();
      });
      
});

d3.json(urlSector, function(SectorData) {
    const dataSource = {
        chart: {
          caption: "Total Market Value by Sector",
          subcaption: "In Millions as of 3/31/20",
          showpercentvalues: "1",
          showLegend: "0",
          defaultcenterlabel: `Total Assets: $${SectorData[9]} Million`,
          aligncaptionwithcanvas: "0",
          captionpadding: "0",
          decimals: "1",
          plottooltext:
          "<b>$percentValue</b> of Total Market Value is the <b>$label</b> Sector",
          centerlabel: "$label: $value",
          theme: "fusion"
        },
        data: SectorData[8]
      };
      
      FusionCharts.ready(function() {
        var myChart = new FusionCharts({
          type: "doughnut2d",
          renderAt: "chart-container2",
          width: "100%",
          height: "500%",
          dataFormat: "json",
          dataSource
        }).render();
      });
});