#!/bin/bash

# Design System Website - Quick Start Script
# This script starts a local web server to run the design system website

echo "🚀 Starting Design System Website..."
echo ""
echo "Opening local server at http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

# Start Python HTTP server
python3 -m http.server 8000
