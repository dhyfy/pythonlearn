# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['七段数码管绘制2.py'],
             pathex=['G:\\python\\Python语言程序设计 嵩天 北京理工大学\\【第5周】函数和代码复用'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='七段数码管绘制2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='修改.ico')
