#!/usr/bin/env python3
import json

# Load the design tokens
with open('design-system-master.json', 'r') as f:
    tokens = json.load(f)

print("/* ========================================")
print("   CSS CUSTOM PROPERTIES (Design Tokens)")
print("   Generated from design-system-master.json")
print("   Using SEMANTIC tokens (Alias), not primitives")
print("   ======================================== */")
print(":root {")

# Helper function to convert token path to CSS variable name
def to_css_var(path):
    return '--' + path.replace('/', '-').replace(' ', '-').replace('(', '').replace(')', '')

# Helper function to get hex value
def get_hex(value):
    if isinstance(value, dict) and 'hex' in value:
        return value['hex']
    return value

print("\n    /* ===== PRIMITIVE COLOR TOKENS ===== */")
print("    /* These are the base colors - use semantic tokens in components */")

# Blue colors
if 'blue' in tokens.get('color', {}):
    print("\n    /* Blue Primitive */")
    for key, val in sorted(tokens['color']['blue'].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999):
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/blue/{key}')}: {hex_val};")

# Neutral colors
if 'neutral' in tokens.get('color', {}):
    print("\n    /* Neutral Primitive */")
    for key, val in sorted(tokens['color']['neutral'].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999):
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/neutral/{key}')}: {hex_val};")

# Basic colors
if 'basic' in tokens.get('color', {}):
    print("\n    /* Basic Primitive */")
    for key, val in tokens['color']['basic'].items():
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/basic/{key}')}: {hex_val};")

# Success colors
if 'success' in tokens.get('color', {}):
    print("\n    /* Success Primitive */")
    for key, val in sorted(tokens['color']['success'].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999):
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/success/{key}')}: {hex_val};")

# Warning colors
if 'warning' in tokens.get('color', {}):
    print("\n    /* Warning Primitive */")
    for key, val in sorted(tokens['color']['warning'].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999):
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/warning/{key}')}: {hex_val};")

# Error colors
if 'error' in tokens.get('color', {}):
    print("\n    /* Error Primitive */")
    for key, val in sorted(tokens['color']['error'].items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999):
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/error/{key}')}: {hex_val};")

print("\n    /* ===== SEMANTIC COLOR TOKENS (USE THESE IN COMPONENTS) ===== */")

# Surface tokens
if 'surface' in tokens.get('color', {}):
    print("\n    /* Surface - Backgrounds */")
    surface = tokens['color']['surface']
    if 'background' in surface:
        for key, val in surface['background'].items():
            if '$value' in val:
                hex_val = get_hex(val['$value'])
                print(f"    {to_css_var(f'color/surface/background/{key}')}: {hex_val};")
    
    if 'button' in surface:
        print("\n    /* Surface - Buttons */")
        for key, val in surface['button'].items():
            if '$value' in val:
                hex_val = get_hex(val['$value'])
                print(f"    {to_css_var(f'color/surface/button/{key}')}: {hex_val};")

# Text tokens
if 'text' in tokens.get('color', {}):
    print("\n    /* Text Colors */")
    text = tokens['color']['text']
    
    # Disable
    if 'disable' in text and '$value' in text['disable']:
        hex_val = get_hex(text['disable']['$value'])
        print(f"    {to_css_var('color/text/disable')}: {hex_val};")
    
    # Heading
    if 'heading' in text:
        for key, val in text['heading'].items():
            if '$value' in val:
                hex_val = get_hex(val['$value'])
                print(f"    {to_css_var(f'color/text/heading/{key}')}: {hex_val};")
    
    # Body
    if 'body' in text:
        for key, val in text['body'].items():
            if '$value' in val:
                hex_val = get_hex(val['$value'])
                print(f"    {to_css_var(f'color/text/body/{key}')}: {hex_val};")
    
    # Link
    if 'link' in text:
        for key, val in text['link'].items():
            if '$value' in val:
                hex_val = get_hex(val['$value'])
                print(f"    {to_css_var(f'color/text/link/{key}')}: {hex_val};")
    
    # On-button
    if 'on-buton' in text:
        for key, val in text['on-buton'].items():
            if '$value' in val:
                hex_val = get_hex(val['$value'])
                print(f"    {to_css_var(f'color/text/on-button/{key}')}: {hex_val};")
    
    # States
    if 'states' in text:
        states = text['states']
        if 'active' in states and '$value' in states['active']:
            hex_val = get_hex(states['active']['$value'])
            print(f"    {to_css_var('color/text/states/active')}: {hex_val};")
        
        if 'information' in states:
            for key, val in states['information'].items():
                if '$value' in val:
                    hex_val = get_hex(val['$value'])
                    print(f"    {to_css_var(f'color/text/states/information/{key}')}: {hex_val};")
        
        if 'success' in states:
            for key, val in states['success'].items():
                if '$value' in val:
                    hex_val = get_hex(val['$value'])
                    print(f"    {to_css_var(f'color/text/states/success/{key}')}: {hex_val};")
        
        if 'warning' in states:
            for key, val in states['warning'].items():
                if '$value' in val:
                    hex_val = get_hex(val['$value'])
                    print(f"    {to_css_var(f'color/text/states/warning/{key}')}: {hex_val};")
        
        if 'error' in states:
            for key, val in states['error'].items():
                if '$value' in val:
                    hex_val = get_hex(val['$value'])
                    print(f"    {to_css_var(f'color/text/states/error/{key}')}: {hex_val};")

# Icons
if 'icons' in tokens.get('color', {}):
    print("\n    /* Icons */")
    for key, val in tokens['color']['icons'].items():
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/icons/{key}')}: {hex_val};")

# Borders
if 'borders' in tokens.get('color', {}):
    print("\n    /* Borders */")
    for key, val in tokens['color']['borders'].items():
        if '$value' in val:
            hex_val = get_hex(val['$value'])
            print(f"    {to_css_var(f'color/borders/{key}')}: {hex_val};")

# Size tokens
if 'size' in tokens:
    print("\n    /* ===== SIZE TOKENS ===== */")
    for key, val in sorted(tokens['size'].items(), key=lambda x: int(x[0]) if x[0].isdigit() else (0 if x[0] == 'none' else 9999)):
        if '$value' in val:
            value = val['$value']
            print(f"    {to_css_var(f'size/{key}')}: {value}px;")

# Typography
if 'type' in tokens:
    print("\n    /* ===== TYPOGRAPHY TOKENS ===== */")
    if 'family' in tokens['type']:
        print("\n    /* Font Families */")
        for key, val in tokens['type']['family'].items():
            if '$value' in val:
                print(f"    {to_css_var(f'type/family/{key}')}: \"{val['$value']}\", -apple-system, BlinkMacSystemFont, sans-serif;")

print("\n    /* ===== DERIVED VALUES ===== */")
print("    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);")
print("    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);")
print("    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);")
print("    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);")
print("    --radius-sm: var(--size-4);")
print("    --radius-md: var(--size-8);")
print("    --radius-lg: var(--size-12);")
print("    --radius-xl: var(--size-16);")
print("    --radius-full: 9999px;")
print("    --transition-fast: 150ms ease;")
print("    --transition-base: 200ms ease;")
print("    --transition-slow: 300ms ease;")
print("    --sidebar-width: 280px;")
print("}")
