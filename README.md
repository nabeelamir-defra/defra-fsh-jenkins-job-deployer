# DEFRA FSH Jenkins Job Deployer

## Setup
Run the following to install the dependencies
```
pip install -r requirements.txt
```
Create a .env file and the following variables
```
JENKINS_URL=<the jenkins url>
JENKINS_USERNAME=<your jenkins username>
JENKINS_PASSWORD=<your jenkins password>
```

## Running
To run you must provide the tag you want to deploy and the environment you want to deploy to (currently DEV or TEST)

```
python3 app.py v1.19.0-rc.0 DEV
```