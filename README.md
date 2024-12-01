
# Data Engineer Tests Part1

This project includes Python scripts and Jupyter notebooks for data analysis and visualization. It uses **Docker** to simplify the setup process, ensuring a consistent and portable environment for all users.

**note**: If you don't have docker installed, you can head over to the [Get Docker](https://docs.docker.com/get-docker/)
page for installation instructions.

## Getting Started
### 1. Clone the repository
```
git clone <repository-url>
```
```
cd test_de_role_pt1
```

### 2. Using Docker
**Build and Run the Project**
1. Build the Docker image:
```
docker compose up --build
```

2. Open Jupyter Notebook:
- Access it in your browser at http://localhost:8888.

### 3. Running Python Scripts
To run a specific Python script inside the Docker container:
1. Start an interactive session:
```
docker run -it test_de_role_pt1 /bin/bash
```
2. Run the script:
```
python src/test_1.py
```
```
python src/test_2.py
```
```
python src/test_3.py
```
```
python src/test_4.py
```
