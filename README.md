# Panoptes Project - Version 1.1

## Overview
Welcome to the Panoptes Project, which leverages Docker to create a dual-container setup incorporating BERT for NLP tasks and a SQL database for robust data management. This branch, version 1.1, introduces enhancements and new features aimed at improving both performance and user experience.

## Project Structure
The project consists of two primary components:
- **Panoptes_BERT**: This component is dedicated to handling all Natural Language Processing tasks. It includes necessary scripts, a Dockerfile, and configurations for deployment.
- **Panoptes_SQL**: Focuses on managing data storage and processing through MySQL, ensuring data integrity and efficient data retrieval.

## Getting Started

### Prerequisites
- Docker must be installed on your machine to run the containers. Docker streamlines the deployment of our applications along with their dependencies.

### Installation
To get started with the Panoptes Project, follow these steps:

1.  **Clone the Repository**:
    Clone the repository to your local machine by running:
    ```bash
    git clone https://github.com/VX1632/Panoptes_Project.git

2.  Navigate to Project Directory:
    Change to the project directory:
    cd Panoptes_Project

3.  Launch Docker Containers:
    Build and start the Docker containers as defined in the docker-compose.yml:
    docker-compose up --build

    Ensure Docker is running on your machine before executing this command.

## Making Changes
If you wish to make changes to the project:

1.  Navigate to the Project Directory (if you are not already there):
    cd Panoptes_Project

2.  Edit or Add Files:
    Make your changes to the files or add new files as necessary.

3.  Rebuild Docker Containers:
    Apply your changes by rebuilding the Docker containers:

## Contributing
To contribute to the project:

1.  Stage Your Changes:
    Add all your changes to the staging area:
    git add .

2.  Commit your Changes:
    git commit -m "Provide a detailed description of your changes"

3.  Push your Changes
    git push origin version_1.1

## Support

For any technical issues or questions, please use the issue tracker on GitHub or contact one of the project maintainers directly.

### Authors

    [Brian Chen, Jean-Pierre Martinez, Ina Shanelle Noceja, Justin Ross]


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This project utilizes several open-source packages and libraries to enhance its functionalities. We are grateful to the developers and maintainers of these tools:

- **Tesseract OCR**: An open-source optical character recognition engine used in our application to extract text from images. More information can be found at [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).

- **libgl1-mesa-glx & libmysqlclient-dev**: These libraries provide necessary graphics support and MySQL database connectivity in a Linux environment, respectively.

- **Git**: Used for version control to manage the development process of our project efficiently. Learn more at [Git SCM](https://git-scm.com/).

- **MySQL & SQLAlchemy**: MySQL is the underlying database management system that stores all our application data, while SQLAlchemy provides a high-level ORM framework to interact with MySQL using Python code, simplifying database manipulation. More details about MySQL are available at [MySQL](https://www.mysql.com/), and you can learn more about SQLAlchemy at [SQLAlchemy](https://www.sqlalchemy.org/).

- **PyTorch**: Utilized for running advanced machine learning models, particularly in processing and interpreting the textual data extracted by Tesseract OCR.

Each of these components plays a vital role in the functionality and efficiency of our project, and their open-source nature has significantly contributed to the progress and success of our development efforts.
We also extend our gratitude to the contributors of the Python packages such as SQLAlchemy and PyTorch, which are critical to our project's operation. Their dedication to open source makes our project possible.










