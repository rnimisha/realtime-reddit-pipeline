# Reddit Data Streaming Pipeline

Data pipeline for ingesting, processing, and visualizing data from a Reddit subreddit in real-time.

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka" alt="Apache Kafka">
  <img src="https://img.shields.io/badge/Apache%20Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black" alt="Apache Spark">
  <img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
  <img src="https://img.shields.io/badge/Reddit-%23FF4500.svg?style=for-the-badge&logo=Reddit&logoColor=white" alt="Reddit">
  <img src="https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
</p>

## Features 📊

- **Reddit Data Ingestion:** Python and PRAW to collect data from a subreddit.
- **Apache Kafka :** Streams Reddit data to for real-time processing.
- **Apache Spark Processing:** Processes streaming data with Apache Spark.
- **MongoDB Storage:** Persists processed data into MongoDB for further analysis and reporting.
- **Streamlit Dashboard:** Visualizes real-time data insights.

## Pipeline Architecture

![Data Pipeline Architecture](https://raw.githubusercontent.com/rnimisha/realtime-reddit-pipeline/main/images/pipeline.jpeg)

## Analytics Dashboard

![Dashboard](https://raw.githubusercontent.com/rnimisha/realtime-reddit-pipeline/main/images/dashboard.gif)

![Dashboard](https://raw.githubusercontent.com/rnimisha/realtime-reddit-pipeline/main/images/dashboard2.gif)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in root of the project

| Name                | Description                                      |
| ------------------- | ------------------------------------------------ |
| CLIENT_SECRET       | Reddit Client Secret.                            |
| CLIENT_ID           | Reddit Client ID.                                |
| USER_AGENT          | Reddit User Agent.                               |
| KAFKA_HOST          | Kafka broker host/IP.                            |
| KAFKA_PORT          | Kafka broker port.                               |
| KAFKA_TOPIC         | Topic to write message on.                       |
| SUBREDDIT           | Subreddit to extract data from.                  |
| MONGO_ROOT_USERNAME | Root user for mongoDB.                           |
| MONGO_ROOT_PASSWORD | Password of root user for mongoDB.               |
| DB_USER             | Username for accessing the MongoDB database.     |
| DB_PASSWORD         | Password for the MongoDB database.               |
| DB_HOST             | Hostname or IP address for the MongoDB database. |
| DB_PORT             | Port number for the MongoDB database.            |
| DB_DATABASE         | Name of the MongoDB database.                    |

## Prerequisites

Before proceeding with this project, ensure you have the following:

- **Git:** Version control. [Download Git](https://git-scm.com/downloads)
- **Docker:** Containerization. [Get Docker](https://www.docker.com/products/docker-desktop)
- **Docker Compose:** Running Multi-container Docker applications. [Install Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the project from the repository.

```bash
  git clone https://github.com/rnimisha/realtime-reddit-pipeline.git

  cd realtime-reddit-pipeline
```

2. Duplicate the `.env.example` file and rename it to `.env`.

```bash
  cp .env.example .env
```

3. Adjust values for environment variables
4. Build images and run the services.

```bash
  docker compose up -d --build
```

5. Access the Streamlit dashboard in your localhost running at port 8501.

## Future Work

- **Fault Tolerance** : Replicate brokers and partion the topic.
- **Data Quality Test** : Write test case to verify data quality.
