import setuptools
import json
import os


thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/package_requirements.txt'
install_requires = [] # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]

if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

with open('./package_setup.json') as json_file:
    setupConfig = json.load(json_file)

with open("README.md", "r") as fh:
    long_description = fh.read()

setupConfig['long_description'] = long_description
setupConfig['packages'] = setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
setupConfig['install_requires'] = install_requires
setuptools.setup(**setupConfig)