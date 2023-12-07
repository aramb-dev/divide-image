from setuptools import setup

APP = ['script.py']

# List of packages to include in the application bundle
PACKAGES = ['PIL']

# List of additional modules to include in the application bundle
INCLUDES = [
    'PyQt5',
    'PySide2',
    'asyncio',  # Added for _overlapped
    'cffi',  # Added for PIL.Image and PIL.PyAccess
    'olefile',  # Added for PIL.FpxImagePlugin and PIL.MicImagePlugin
    'platformdirs',  # Added for pkg_resources._vendor.platformdirs.__main__
    'PIL.ImageTk',  # Added for cffi (conditional import)
    'jnius',  # Added for pkg_resources._vendor.platformdirs.android (conditional import)
    'typing_extensions',  # Added for pkg_resources._vendor.packaging.metadata (conditional import)
]

# Path to the ICNS file for the application's icon
ICONFILE = 'logo.icns'

# Dictionary to specify the Info.plist file settings
PLIST = {
    'CFBundleIdentifier': 'com.aramservices.image-splitter',
    'CFBundleName': 'Image Splitter',
    'CFBundleDisplayName': 'Image Splitter',
    'CFBundleVersion': '1.0',
    'CFBundleShortVersionString': '1.0',
    'CFBundleGetInfoString': 'This app splits images into rows of your choice.',
    'CFBundleIconFile': 'logo.icns',
}

# Set the optimization level to 2 (maximum optimization)
OPTIMIZE = 0

DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': PACKAGES,
    'excludes': [],
    'includes': INCLUDES,
    'iconfile': ICONFILE,
    'plist': PLIST,
    'resources': [],
    'site_packages': True,
    'compressed': False,
    'optimize': OPTIMIZE,
    'arch_flags': ['-arch arm64', '-arch x86_64'],  # Specify architecture flags for Universal binary
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
