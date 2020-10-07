// Sector URL
var urlSector = "http://127.0.0.1:5000/sector";

// Asset Donut Chart
d3.json(urlSector, function(SectorData) {

    console.log(SectorData[7])

    // Add commas as thousands separators to asset total to display in center of donut chart
    var AssetsTotal = SectorData[7].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");

    // Set up fusionchart
    const dataSource = {
        chart: {
          caption: "Total Assets by Sector",
          subcaption: "In Millions",
          showpercentvalues: "1",
          showLegend: "0",
          defaultcenterlabel: `Total Assets: $${AssetsTotal} Million`,
          aligncaptionwithcanvas: "0",
          captionpadding: "0",
          decimals: "1",
          formatNumberScale: "0",
          plottooltext:
            "<b>$percentValue</b> of Assets owned by <b>$label</b> Sector",
          centerlabel: "$label: $$value Million",
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

// Market Value donut chart
d3.json(urlSector, function(SectorData) {

    var MVTotal = SectorData[9].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");

    const dataSource = {
        chart: {
          caption: "Total Market Value by Sector",
          subcaption: "In Millions as of 3/31/20",
          showpercentvalues: "1",
          showLegend: "0",
          defaultcenterlabel: `Total Assets: $${MVTotal} Million`,
          aligncaptionwithcanvas: "0",
          captionpadding: "0",
          decimals: "1",
          formatNumberScale: "0",
          plottooltext:
          "<b>$percentValue</b> of Total Market Value is the <b>$label</b> Sector",
          centerlabel: "$label: $$value Million",
          theme: "fusion"
        },
        data: SectorData[8]
      };
      
      FusionCharts.ready(function() {
        var myChart = new FusionCharts({
          type: "doughnut2d",
          renderAt: "chart-container2",
          width: "100%",
          height: "205%",
          dataFormat: "json",
          dataSource
        }).render();
      });
});