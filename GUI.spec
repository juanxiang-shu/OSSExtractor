# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

py_files = [
    'GUI.py',
    'analysis.py',
    'apriori_Rea_Sub.py',
    'apriori_Rea_Tem.py',
    'apriori_Tem_Sub.py',
    'blank_page.py',
    'chartdialog_analysis.py',
    'chartdialog_statistics.py',
    'Compounds.py',
    'data_processor.py',
    'element_definitions.py',
    'Fre_profor_total.py',
    'Fre_rea_total.py',
    'Fre_sub_total.py',
    'Fre_Tem_total.py',
    'pdf.py',
    'Precursors.py',
    'Product.py',
    'Product_form.py',
    'Reactions.py',
    'results_dialog.py',
    'statistics.py',
    'Temperature_Substrate.py',
]

add_files = [('images\\1.ico', 'images'),]

a = Analysis(
    py_files,
    pathex=['E:\\project\\pycharm\\untitled'],
    binaries=[],
    datas=add_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='OSSExtractor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='E:\\project\\pycharm\\untitled\\images\\1.ico'
)
