## Docker app for testing github workflows

### running the app
```python app.py```

### building the docker image
```
docker build -t testapp .
```

### running the docker container
```
docker run --name dockertest -d --rm -p 8070:5000 testapp
```

### Docker Setup In EC2 commands to be Executed

#### optional command
sudo apt-get update && sudo apt-get upgrade -y


#### required
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
