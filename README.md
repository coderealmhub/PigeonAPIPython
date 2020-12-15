# Pigeon API Python

API Python para comuniação com o aplicativo [Pigeon SMS Gateway](https://github.com/coderealmhub/PigeonSMSGateway).


# Settings

## Virtualenv

    virtualenv .venv
    
    source .venv/bin/activate

## Install Requirements

## Generate SSL Https

    openssl req -nodes -new -x509 -keyout server.key -out server.cert

# Start Server

## Http

    bash run_http.sh

## Https

    bash run_https.sh

# TODO

[Admin API](https://github.com/long2ice/fastapi-admin)