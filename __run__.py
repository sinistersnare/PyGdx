'''
Created on Oct 14, 2013

This module can be thought of as the main method. The entry point to the created JAR.
Notice the `if __name__ =='__run__':` as opposed to '__main__' for reference :D

@author: sinistersnare
'''


from com.badlogic.gdx.backends.lwjgl import LwjglApplicationConfiguration, LwjglApplication
from Gdx import PyGdx


def main():
    
    cfg = LwjglApplicationConfiguration()
    cfg.title = "PyGdx";
    cfg.width = 800
    cfg.height = 480
    
    LwjglApplication(PyGdx(), cfg)
if __name__ == '__run__':
    """
    notice __run__ as opposed to __main__
    think of this as the jar'd equivalent
    """ 
    main()
    
