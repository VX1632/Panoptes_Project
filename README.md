# Panoptes_Project
Software Development - Panoptes Schedule Processor (BERT)

## Overview
The Panoptes Project is designed to leverage advanced BERT models for text analysis and connect seamlessly with a MySQL database for data management. This project uses Docker containers to ensure easy setup and reproducibility.

## Features
- BERT-based text processing.
- Integration with MySQL for persistent data storage.
- Dockerized environment for easy setup and cross-platform compatibility.

## Technology Stack
- Python 3.8
- MySQL
- Docker & Docker Compose

## Directory Structure
C:\Panoptes_Project
│
├── docker-compose.yml
│
├── Panoptes_BERT
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── AIAI_World_Tour.jpg
│   ├── Handwriting.jpg
│   ├── motor_bella.jpg
│   └── Rebuild.sh
│
└── Panoptes_SQL
    └── init.sql


## Getting Started

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your_username/Panoptes_Project.git

2. Navigate to the project directory
   cd Panoptes_Project

3. Start the services
   docker-compose up --build


   
Usage 

This is still under development, this is only the backend part of the project and the front-end is still being developed and hammered out.

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    1. Fork the Project
    2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
    3. Commit your Changes (git commit -m 'Add some AmazingFeature')
    4. Push to the Branch (git push origin feature/AmazingFeature)
    5. Open a Pull Request   

License

Distributed under the MIT License. See LICENSE for more information.


Acknowledgements
  Hugging Face: BERT (Bidirectional Encoder Representations from Transformers) model
    dbmdz/bert-large-cased-finetuned-conll03-english is a pre-trained model available through the Hugging Face model hub

  Hugging Face Transformers Library

  Additional Team Member's git will be added...

Source:

    The transformers library by Hugging Face is a popular and comprehensive library that provides state-of-the-art general-purpose architectures for Natural Language Processing (NLP), including BERT, GPT, RoBERTa, and others.
    The library facilitates the use of many pre-trained models that are trained on a vast range of datasets for various tasks (e.g., text classification, token classification, and question answering).
    
