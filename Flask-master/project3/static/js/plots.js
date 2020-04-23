//https://community.plotly.com/t/add-labels-to-time-series-read-from-csv/11586
// USA plot
function buildPlot() {
  let d3;
  let Plotly;

    /* data route */
  const url = "/api/usa";
  d3.json(url).then(function(buf){ 
  var x_time = [], y_priceClose = [], y_covidUS = [];
  for (var i = 0; i < buf.length; i++) {
    row = buf[i];
    x_time.push( row['time'] );
    y_priceClose.push( row['last'] );
    y_covidUS.push( row['cases'] );
  }
  var traceDow = {
    x: x_time,
    y: y_priceClose,
    mode: 'lines+markers',
    type: 'scatter',
    name: 'Dow Jones Close Price'
  };
  var traceCovidUS = {
    x: x_time,
    y: y_covidUS,
    mode: 'lines+markers',
    type: 'scatter',
    name: 'COVID-19 Reported Cases'
  };
  var data = [traceDow, traceCovidUS];
  var layout = {
    yaxis: {
       tickformat: '.0', 
    title: "USA Covid-19 Cases & DOW Jones Close Price",
    xaxis: { title: "X-Axis" },
    yaxis: { title: "Y-Axis"}
    }
  };
  Plotly.newPlot('plot-us', data, layout);
  } );

}

buildPlot();



// Korea plot
  const url = "/api/kr";
  d3.json(url2.then(function(buf){ 
  var x_time1 = [], y_priceClose1 = [], y_covidKorea = [];
  for (var i = 0; i < buf.length; i++) {
    row = buf[i];
    x_time1.push( row['time'] );
    y_priceClose1.push( row['last'] );
    y_covidKorea.push( row['cases'] );
  }
  var traceKOSPI = {
    x: x_time1,
    y: y_priceClose1,
    mode: 'lines+markers',
    type: 'scatter',
    name: 'KOSPI Close Price'
  };
  var traceCovidKorea = {
    x: x_time1,
    y: y_covidKorea,
    mode: 'lines+markers',
    type: 'scatter',
    name: 'COVID-19 Reported Cases'
  };

  var data = [traceKOSPI, traceCovidKorea];
  var layout = {
    yaxis: {
       tickformat: '.0', 
    title: "South Korea Covid-19 Cases & KOSPI Close Price",
    xaxis: { title: "X-Axis" },
    yaxis: { title: "Y-Axis"}
    }
  };
  Plotly.newPlot('plot-kr', data, layout);
});


// UK plot
    const url = "/api/uk";
    d3.json(url).then(function(buf){ 
    var x_time2 = [], y_priceClose2 = [], y_covidUK = [];
    for (var i = 0; i < buf.length; i++) {
      row = buf[i];
      x_time2.push( row['time'] );
      y_priceClose2.push( row['last'] );
      y_covidUK.push( row['cases'] );
    }
    var traceFTSE = {
      x: x_time2,
      y: y_priceClose2,
      mode: 'lines+markers',
      type: 'scatter',
      name: 'FTSE Close Price'
    };
    var traceCovidUK = {
      x: x_time2,
      y: y_covidUK,
      mode: 'lines+markers',
      type: 'scatter',
      name: 'COVID-19 Reported Cases'
    };
    var data = [traceFTSE, traceCovidUK];
    var layout = {
      yaxis: {
         tickformat: '.0', 
      title: "United Kingdom Covid-19 Cases & FTSE Close Price",
      xaxis: { title: "X-Axis" },
      yaxis: { title: "Y-Axis"}
      }
    };
    Plotly.newPlot('plot-uk', data, layout);
});