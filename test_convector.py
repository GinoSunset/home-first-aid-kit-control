import os

import cv2
import pytest
from cv2 import data

from decode_datamatrix_code import decode_image


def test_datamatrix_convector():
    path_to_image = os.path.join("example", "r_dm.png")
    list_datamatrix = decode_image(cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED))
    decode_text = "010460180800004721DpNcisy6vCERY91EE0692SPAXkDQJdS4VIj+rtATpWbOF8u0mdHdDJyaOJb2avNQ=" 
    assert any(map(lambda datamatrix: decode_text in datamatrix[0].decode(), list_datamatrix))

@pytest.mark.skip
def test_datamatrix_convector_hard_images():
    path_to_image = os.path.join("example", "datamatrix.png")
    list_datamatrix = decode_image(cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED))
    decode_text = "010460180800004721DpNcisy6vCERY91EE0692SPAXkDQJdS4VIj+rtATpWbOF8u0mdHdDJyaOJb2avNQ=" 
    assert any(map(lambda datamatrix: decode_text in datamatrix[0].decode(), list_datamatrix))
