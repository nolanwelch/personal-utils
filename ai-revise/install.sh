#!/bin/bash

CFG_FILE=~/.bashrc
PACKAGE_ALIAS='alias airevise="python -m airevise"'

python -m pip install -r airevise/requirements.txt
python -m pip install airevise/

if ! grep -q "$PACKAGE_ALIAS" "$CFG_FILE"; then
    echo "$PACKAGE_ALIAS" >>"$CFG_FILE"
fi

echo "Installation complete!"
