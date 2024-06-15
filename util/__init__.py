from os.path import dirname, basename
from glob import glob

files = glob(f"{dirname(__file__)}/*.py")
__all__ = [ basename(f).rsplit('.', 1)[0] 
	for f in files if not f.startswith('__') 
]
