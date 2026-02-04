#!/bin/bash

# Generate CSS variables from design-system-master.json

echo "/* ========================================"
echo "   CSS CUSTOM PROPERTIES (Design Tokens)"
echo "   Auto-generated from design-system-master.json"
echo "   ======================================== */"
echo ":root {"

# Extract color tokens
echo ""
echo "    /* ===== COLOR TOKENS ===== */"

# Blue colors
echo ""
echo "    /* Blue */"
jq -r '.color.blue | to_entries[] | "    --color-blue-\(.key): \(.value.$value.hex);"' design-system-master.json

# Neutral colors
echo ""
echo "    /* Neutral */"
jq -r '.color.neutral | to_entries[] | "    --color-neutral-\(.key): \(.value.$value.hex);"' design-system-master.json

# Basic colors
echo ""
echo "    /* Basic */"
jq -r '.color.basic | to_entries[] | "    --color-\(.key): \(.value.$value.hex);"' design-system-master.json

# Success colors
echo ""
echo "    /* Success */"
jq -r '.color.success | to_entries[] | "    --color-success-\(.key): \(.value.$value.hex);"' design-system-master.json

# Warning colors
echo ""
echo "    /* Warning */"
jq -r '.color.warning | to_entries[] | "    --color-warning-\(.key): \(.value.$value.hex);"' design-system-master.json

# Error colors
echo ""
echo "    /* Error */"
jq -r '.color.error | to_entries[] | "    --color-error-\(.key): \(.value.$value.hex);"' design-system-master.json

# Size tokens
echo ""
echo "    /* ===== SIZE TOKENS ===== */"
jq -r '.size | to_entries[] | select(.value."$value" != null) | "    --size-\(.key): \(.value.$value)px;"' design-system-master.json

# Typography tokens
echo ""
echo "    /* ===== TYPOGRAPHY TOKENS ===== */"
echo ""
echo "    /* Font Families */"
jq -r '.type.family | to_entries[] | "    --font-\(.key): '\''\(.value.$value)'\'', -apple-system, BlinkMacSystemFont, sans-serif;"' design-system-master.json

echo ""
echo "    /* Font Weights */"
jq -r '.type.weight.heading | to_entries[] | "    --font-weight-heading-\(.key): \(.value.$value);"' design-system-master.json 2>/dev/null || true
jq -r '.type.weight.body | to_entries[] | "    --font-weight-body-\(.key): \(.value.$value);"' design-system-master.json 2>/dev/null || true

echo "}"
