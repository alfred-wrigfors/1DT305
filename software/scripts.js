const envChart = create_chart();
update_data();
setInterval(update_data, 1000);


function update_data() {
    console.log("Updating data...");
    const data = fetch_data();
    display_data(data)
}

function fetch_data() {
    return mock_data();
}

function display_data(data){

    // Update the chart datasets with new data
    envChart.data.datasets[0].data = data.water_temp;
    envChart.data.datasets[1].data = data.air_temp;
    envChart.data.datasets[2].data = data.air_humidity;

    const timestamps = data.water_temp.map(d => new Date(d.x).getTime());

    envChart.options.scales.x.min = new Date(Math.min(...timestamps));
    envChart.options.scales.x.max = new Date(Math.max(...timestamps));

    // Redraw the chart
    envChart.update();
}

function create_chart(){
    const timeLabels = Array.from({ length: 100 }, (_, i) => `${i + 1}h`);
    const ctx = document.getElementById('envChart').getContext('2d');
    const chart = new Chart(ctx, {
      type: 'line',
      data: {
        datasets: [
          {
            label: 'Water Temp (°C)',
            data: [],
            borderColor: '#0077be',
            backgroundColor: 'rgba(0, 119, 190, 0.1)',
            tension: 0.4,
            pointRadius: 0,
            pointHoverRadius: 4
          },
          {
            label: 'Air Temp (°C)',
            data: [],
            borderColor: '#ffa600',
            backgroundColor: 'rgba(255, 166, 0, 0.1)',
            tension: 0.4,
            pointRadius: 0,
            pointHoverRadius: 4
          },
          {
            label: 'Humidity (%)',
            data: [],
            borderColor: '#00aa66',
            backgroundColor: 'rgba(0, 170, 102, 0.1)',
            tension: 0.4,
            yAxisID: 'y1',
            pointRadius: 0,
            pointHoverRadius: 4
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
            x: {
                type: 'time',
                time: {
                unit: 'minute', // or 'second', 'hour', 'day', etc.
                tooltipFormat: 'HH:mm:ss',
                displayFormats: {
                    minute: 'HH:mm',
                    second: 'HH:mm:ss'
                }
                },
                title: {
                display: true,
                text: 'Time'
                }
            },
          y: {
            type: 'linear',
            position: 'left',
            title: {
              display: true,
              text: '°C'
            },
            grid: {
              drawBorder: false
            }
          },
          y1: {
            type: 'linear',
            position: 'right',
            title: {
              display: true,
              text: '% Humidity'
            },
            grid: {
              drawOnChartArea: false
            }
          }
        },
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              boxWidth: 12,
              boxHeight: 12,
              padding: 15
            }
          },
          tooltip: {
            mode: 'index',
            intersect: false
          }
        },
        interaction: {
          mode: 'nearest',
          axis: 'x',
          intersect: false
        },
        ticks: {
            maxTicksLimit: 8
            }
      }
    });

    return chart;
}

// MOCK DATA
function mock_data(){
    const now = Date.now();
    const intervalMs = 1000 * 60*60; // 1 second intervals
    const count = 48;

    const waterTemps = Array.from({ length: count }, (_, i) => ({
        x: new Date(now - (count - i) * intervalMs).toISOString(), // or use new Date(...)
        y: Math.random() * 2 + 18
    }));

    const airTemps = Array.from({ length: count }, (_, i) => ({
        x: new Date(now - (count - i) * intervalMs).toISOString(),
        y: Math.random() * 2 + 25
    }));

    const humidityVals = Array.from({ length: count }, (_, i) => ({
        x: new Date(now - (count - i) * intervalMs).toISOString(),
        y: Math.random() * 2 + 50
    }));

    return {
        water_temp: waterTemps,
        air_temp: airTemps,
        air_humidity: humidityVals
    };
}