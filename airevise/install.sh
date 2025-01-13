#!/bin/bash

CFG_FILE=~/.bashrc
PACKAGE_ALIAS='alias airevise="python -m airevise"'

python -m pip install -r requirements.txt
python -m pip install .

if ! grep -q "$PACKAGE_ALIAS" "$CFG_FILE"; then
    echo "$PACKAGE_ALIAS" >>"$CFG_FILE"
fi

echo "Installation complete!"
