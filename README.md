# FastAPI CRUD Application with Docker Deployment

## Overview

This project demonstrates the development of a CRUD (Create, Read, Update, Delete) application using FastAPI. It also includes image processing functionality using OpenCV. Additionally, the project showcases deployment using Docker and Ubuntu.

## Part 1: Application Development

### Features

- **User Management**: CRUD operations for managing users.
- **Authentication**: Token-based authentication using OAuth2.
- **Image Processing**: Functionality to process images using OpenCV.

### Endpoints

- `/users`: CRUD endpoints for user management.
- `/token`: Endpoint for generating authentication tokens.
- `/process_image`: Endpoint for image processing.

####  API Endpoints
- User Management
- Create User: POST /users/
  
- Retrieve User: GET /users/{user_id}
- Update User: PUT /users/{user_id}
- Delete User: DELETE /users/{user_id}
- Search Users: GET /users/search/?name={search_query}

####  Authentication
- Generate Token: POST /token

####  Image Processing
- Process Image: POST /process_image/
![image](https://github.com/abdullah19191/ML_Test/assets/71758955/f685ebde-50ff-4d50-bc06-375f6271121f)


### Technologies Used

- FastAPI
- SQLAlchemy
- OAuth2
- OpenCV
- Python

### Running the Application

To run the application locally:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Start the FastAPI application using `uvicorn main:app --reload`.

## Part 2: Deployment with Docker and Ubuntu

### Docker Setup

- Dockerfile: Configuration for building the Docker image.
- docker-compose.yml: Docker Compose file for managing the application and database containers.

### Deployment Steps

1. Install Docker and Docker Compose on the host machine.
2. Build the Docker image using `docker-compose build`.
3. Start the application containers using `docker-compose up`.

### Accessing the Application

Once the containers are running, you can access the application at `http://localhost:8000`.

## Video Demonstrations

## Part 1: Application Development
  

https://github.com/abdullah19191/ML_Test/assets/71758955/fd30537e-6518-49ed-a46e-b1cc8c15ef7f


## Part 2: Deployment with Docker and Ubuntu



https://github.com/abdullah19191/ML_Test/assets/71758955/4bd63525-753c-4428-a80e-373d24a31245

