// Sector URL
var urlSector = "http://127.0.0.1:5000/sector";

d3.json(urlSector, function(SectorData) {

    console.log(SectorData)

    const dataSource = {
        chart: {
          caption: "Revenue & Profits",
          subcaption: "In Millions",
          placevaluesinside: "1",
          showvalues: "0",
          plottooltext: "<b>$dataValue</b> for the $label sector in $seriesName",
          theme: "fusion"
        },
        categories: [
          {
            category: SectorData[3]
          }
        ],
        dataset: [
          {
            seriesname: "Revenue",
            data: SectorData[2]
          },
          {
            seriesname: "Profit",
            data: SectorData[4]
          }
        ],
      };
      
      FusionCharts.ready(function() {
        var myChart = new FusionCharts({
          type: "msbar2d",
          renderAt: "chart-container",
          width: "100%",
          height: "500%",
          dataFormat: "json",
          dataSource
        }).render();
      });
      
});

d3.json(urlSector, function(SectorData) {
    const dataSource = {
        chart: {
          caption: "Average Change in Profit by Sector",
          subcaption: "As Compared to 2019",
          yaxisname: "Percent Change",
          aligncaptionwithcanvas: "0",
          plottooltext: "<b>$dataValue</b>% change",
          theme: "fusion"
        },
        data: SectorData[5]
      };
      
      FusionCharts.ready(function() {
        var myChart = new FusionCharts({
          type: "bar2d",
          renderAt: "chart-container2",
          width: "100%",
          height: "500%",
          dataFormat: "json",
          dataSource
        }).render();
      });
});