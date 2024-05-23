# Weather Data Extraction and Visualization Project

## Overview
This project focuses on extracting weather data from the OpenWeatherAPI using Node-RED flow which runs every hour, and process the extracted data using Python scripts. The processed data is then visualized on a dashboard using Observable Plot.

![image](https://github.com/Revalorise/node-red-weather-api/assets/82700651/b1fd45ec-b613-400e-ad76-3feccd9c0821)
## Features
- **[Data Extraction]**: Utilizes Node-RED flow to fetch weather data from the OpenWeatherAPI, enabling real-time access to weather information.
- **[Data Processing]**: Python scripts are employed to process the extracted weather data, performing necessary transformations and calculations.
- **[Visualization]**: The processed weather data is visualized on a dashboard using Observable Plot, allowing users to intuitively comprehend weather trends and patterns.

## Project Components
- Node-RED Flow: Responsible for fetching weather data from the OpenWeatherAPI, ensuring seamless data acquisition.
- Python Scripts: Perform data processing tasks such as data transformation, calculation, and analysis, enhancing the usability of the extracted weather data.
- Observable Dashboard: Utilizes Observable Plot to create an interactive and visually appealing dashboard for presenting the processed weather data, facilitating insightful data exploration and analysis.

## Project Structure
- **[Dashboard folder]**: Contains Observable framework code written in JavaScript, forming the interactive dashboard for visualizing weather data.
- **[Data Transformation folder]**: Houses Python scripts responsible for transforming both current and forecast weather data extracted from Node-RED flows.
- **[Error Log folder]**: Stores error logs generated during the data transformation stage. These logs are instrumental for troubleshooting and debugging potential issues.
- **[Metadata folder]**: Stores metadata indicating the timestamp at which both current and forecast weather data were fetched and subsequently transformed.
- **[Weather Data folder]**: Contains raw weather data extracted from the OpenWeatherAPI through Node-RED flows, serving as the primary source for data processing and visualization.

## Dashboard
![image](https://github.com/Revalorise/node-red-weather-api/assets/82700651/756d71ad-3274-49f0-a10c-5dfe9ac2fbce)
