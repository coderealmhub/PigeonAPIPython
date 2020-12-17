# Pigeon API Python

API Python para comuniação com o aplicativo [Pigeon SMS Gateway](https://github.com/coderealmhub/PigeonSMSGateway).


# Settings

## Virtualenv

    virtualenv .venv
    
    source .venv/bin/activate

## Install Requirements

### Manual

    pip3 install fastapi --user

    pip3 install uvicorn --user

    pip3 install sqlalchemy --user

    pip3 install mysql-connector-python --user

    pip3 install bcrypt --user

    pip3 install async-exit-stack async-generator --user

    pip3 install pyjwt --user

### Auto

    pip3 install -r requirements.txt --user

    
## Generate SSL Https

    openssl req -nodes -new -x509 -keyout server.key -out server.cert

or install Letsencrypt

    sudo apt install certbot
    sudo apt install python3-certbot-apache
    sudo certbot --apache -d your_domain.com

# Start Server

    bash run.sh


# TODO

[Admin API](https://github.com/long2ice/fastapi-admin)