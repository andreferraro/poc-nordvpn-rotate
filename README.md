# POC Sidecar

POC que implementa endpoints para rotacionar o IP da máquina usando NordVPN.
A rotação do IP deverá ser dentro de uma imagem Docker.

## Requirements

Instalar o fork do nord_swith:

```bash
.venv/bin/python3 -m pip install https://github.com/andreferraro/NordVPN-switcher/archive/refs/tags/0.3.1b.zip
```

## Usage

### Local

```bash
curl -X GET http://localhost:5000/ip
```
