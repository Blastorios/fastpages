'''ReSize Images Programmatically
Created by @Blastorios
Created on 28/03/21'''

from typing import Union, Tuple
from pathlib import Path

from PIL import Image

SET_SIZE = (1486, 804)

class ReShape(object):
    """Simple Resize Object"""
    
    def __init__(self, file_path: Union[Path, str]):
        self.path = Path(file_path)
        self.image = Image.open(self.path)
    
    def __del__(self):
        try:
            new_image.close()
        except:
            pass
        try:
            self.image.close()
        except:
            pass
    
    def _resize(self, image, size: Tuple[int] = SET_SIZE):
        return image.resize(size)
    
    def store_new_size(self, location_name: str):
        self.new_image = self._resize(self.image)
        self.new_image.save(location_name)
