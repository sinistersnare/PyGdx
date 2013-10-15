#!python
'''
Created on Oct 14, 2013
Stolen from jimbaker/clamped on github because hes smart and got this working
@author: sinistersnare
'''



import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "PyGDX",
    version = "0.1",
    packages = ['Gdx,py'], #was find_packages()
    install_requires = ["clamp>=0.2"],
    clamp = ["Gdx"],
)
