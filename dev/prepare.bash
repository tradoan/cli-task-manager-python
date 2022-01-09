#!/usr/bin/env bash

set -Eeuxo pipefail

DIR="$(dirname "$(readlink -f "$0")")"
pushd ${DIR}

python3 -m venv "venv"

source "venv/bin/activate"

python3 -m pip install --upgrade pip setuptools wheel

#python3 -m pip install --upgrade --requirement "${DIR}/requirements.txt"
poetry install
popd