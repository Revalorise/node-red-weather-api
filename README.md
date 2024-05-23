# Weather Data Extraction and Visualization Project

## Overview
This project focuses on extracting weather data from the OpenWeatherAPI using Node-RED flow which runs every hour, and process the extracted data using Python scripts. The processed data is then visualized on a dashboard using Observable Plot.

![image](https://github.com/Revalorise/node-red-weather-api/assets/82700651/4562b7bd-dd5e-4271-8df3-65dab4b02774)
## Features
- **[Data Extraction]**: Utilizes Node-RED flow to fetch weather data from the OpenWeatherAPI, enabling real-time access to weather information.
- **[Data Processing]**: Python scripts are employed to process the extracted weather data, performing necessary transformations and calculations.
- **[Visualization]**: The processed weather data is visualized on a dashboard using Observable Plot, allowing users to intuitively comprehend weather trends and patterns.
- **[Notification]**: Notify user on LINE application whether it's hot or cold outside.

## Line Notify
- Uses the LINE Messaging API to notify users when the temperature crosses certain thresholds. The script check the temperature at regular intervals and send notifications under the following conditions:
  - Hot Threshold: Notify the user when the temperature exceeds 30°C.
  - Cold Threshold: Notify the user when the temperature drops below 25°C.
- ## (For Demonstration Purpose Only!)
- ![image](https://github.com/Revalorise/node-red-weather-api/assets/82700651/91dfa611-1371-45b7-a532-2fdbb84ef8f7)

## Project Components
- Node-RED Flow: Responsible for fetching weather data from the OpenWeatherAPI, ensuring seamless data acquisition.
- Python Scripts: Perform data processing tasks such as data transformation, calculation, and analysis, enhancing the usability of the extracted weather data.
- Observable Dashboard: Utilizes Observable Plot to create an interactive and visually appealing dashboard for presenting the processed weather data, facilitating insightful data exploration and analysis.
- LINE Notify: Notify user when the temperature reaches its threshold which is hot when its [>30°C], and cold when its [<25°C].

## Project Structure
- **[Dashboard folder]**: Contains Observable framework code written in JavaScript, forming the interactive dashboard for visualizing weather data.
- **[Data Transformation folder]**: Houses Python scripts responsible for transforming both current and forecast weather data extracted from Node-RED flows.
- **[Error Log folder]**: Stores error logs generated during the data transformation stage. These logs are instrumental for troubleshooting and debugging potential issues.
- **[Line Messaging folder]**: Contains Python script that publishes temperature value and a LINE Notify scripts.
- **[Metadata folder]**: Stores metadata indicating the timestamp at which both current and forecast weather data were fetched and subsequently transformed.
- **[Weather Data folder]**: Contains raw weather data extracted from the OpenWeatherAPI through Node-RED flows, serving as the primary source for data processing and visualization.

## Dashboard
![image](https://github.com/Revalorise/node-red-weather-api/assets/82700651/756d71ad-3274-49f0-a10c-5dfe9ac2fbce)
