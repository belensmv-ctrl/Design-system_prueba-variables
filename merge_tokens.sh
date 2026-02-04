#!/bin/bash

# Use jq to merge the two JSON files
jq -s '.[0] * .[1]' "Valor.tokens.json" "Valor.tokens 2.json" > "design-system-master.json"

echo "✓ Successfully merged both files into design-system-master.json"
