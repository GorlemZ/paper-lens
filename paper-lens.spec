# -*- mode: python ; coding: utf-8 -*-

import spacy
import os
spacy_model_path = spacy.util.get_package_path('en_core_web_sm')

# Package all files in the model directory
spacy_model_files = []
for dirpath, dirnames, filenames in os.walk(str(spacy_model_path)):
    for filename in filenames:
        source_path = os.path.join(dirpath, filename)
        target_path = os.path.relpath(source_path, str(spacy_model_path))
        spacy_model_files.append((source_path, os.path.join('en_core_web_sm', target_path)))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=spacy_model_files,  # Use the expanded model files
    hiddenimports=['en_core_web_sm'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='paper-lens',
    debug=True,  # Change to True
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Change to True for seeing errors
    # ...
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='paper-lens',
)

# Add a BUNDLE section for macOS
app = BUNDLE(
    exe,
    name='paper-lens.app',
    icon=None,
    bundle_identifier=None,
)
