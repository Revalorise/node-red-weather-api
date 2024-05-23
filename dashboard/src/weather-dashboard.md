# Bangkok Weather ⛅

```js
const currentTime = new Date();
```

<h3 class="orange">Current time: ${currentTime}</h3>
<hr>
<h1 class="blue">Current Weather</h1>

```js
const currentWeather = FileAttachment("./data/current_Thai_weather_transformed.json").json();
const forecastWeather = FileAttachment("./data/forecast_Thai_weather_transformed.json").json();
```

```js
function capitalizeWords(str) {
    return str.split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}
```

<div class="grid grid-cols-2">
  <div class="card">
    <h1 class="blue">Information:</h1>
    <table>
      <tr>
        <td align="center"><h2>Location:</h2></td>
        <td align="center"><h2>${currentWeather.name}</h2></td>
      </tr>
      <tr>
        <td align="center"><h2>Last Updated:</h2></td>
        <td align="center"><h2>${currentWeather.dt}</h2></td>
      </tr>
      <tr>
        <td align="center"><h2>Weather:</h2></td>
        <td align="center"><h2>${capitalizeWords(currentWeather.weather[0].description)}</h2></td>
      </tr>
      <tr>
        <td align="center"><h2>Sunrise:</h2></td>
        <td align="center"><h2>${currentWeather.sys.sunrise}</h2></td>
      </tr>
      <tr>
        <td align="center"><h2>Sunset:</h2></td>
        <td align="center"><h2>${currentWeather.sys.sunset}</h2></td>
      </tr>
    </table>
  </div>
  <div class="card">
    <table>
    <tr>
        <td align="center"><h1 class="blue">Temperature:</h1></td>
        <td align="left"><h1 class="yellow">${currentWeather.main.temp}°C</h1></td>
      </tr>
      <tr>
        <td align="center"><h1 class="blue">Feels Like:</h1></td>
        <td align="left"><h1 class="yellow">${currentWeather.main.feels_like}°C</h1></td>
      </tr>
      <tr>
        <td align="center"><h1 class="blue">Min Temperature:</h1></td>
        <td align="left"><h1 class="yellow">${currentWeather.main.temp_min}°C</h1></td>
      </tr>
      <tr>
        <td align="center"><h1 class="blue">Max Temperature:</h1></td>
        <td align="left"><h1 class="yellow">${currentWeather.main.temp_max}°C</h1></td>
      </tr>
      </table>
  </div>
</div>

<hr>
<h1 class="blue">5 Days weather forecast</h1>

```js
const forecastData = forecastWeather.list.map(d => ({
  ...d,  
  date: new Date(d.dt_txt),
  temp: d.main.temp,
  feels_like: d.main.feels_like,
}));
```

```js
Plot.plot({
      title: "5 day / 3 hour forecast",
      width,
      x: {
        type: "time",
        label: "Date",
        ticks: d3.timeHour.every(12), // Set interval to 6 hours
        tickFormat: d3.timeFormat("%a %d | %H:%M"),
        tickRotate: 0
      },
      y: {
          grid: true, 
          label: "Temperature °C",
      },
      color: {
        type: "ordinal",
        legend: true,
        domain: ["Temperature", "Feels Like"],
        range: ["#68cc95", "#a6271e"]
      },
      marks: [
        Plot.ruleY([0]),
        Plot.lineY(forecastData, {x: "date", y: "temp", stroke: "#68cc95", strokeWidth: 2, tip: true}),
        Plot.lineY(forecastData, {x: "date", y: "feels_like", stroke: "#a6271e", strokeWidth: 2}),
      ]
    })
```