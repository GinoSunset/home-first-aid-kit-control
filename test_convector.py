import os

import cv2
import pytest

from datetime import date
from decode_datamatrix_code import decode_image


def test_datamatrix_convector():
    path_to_image = os.path.join("example", "r_dm.png")
    list_datamatrix = decode_image(cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED))
    decode_text = "010460180800004721DpNcisy6vCERY91EE0692SPAXkDQJdS4VIj+rtATpWbOF8u0mdHdDJyaOJb2avNQ="
    assert any(
        map(lambda datamatrix: decode_text in datamatrix[0].decode(), list_datamatrix)
    )


def test_datamatrix_convector_with_tantum():
    path_to_image = os.path.join("example", "tantim_2.jpeg")
    list_datamatrix = decode_image(cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED))
    decode_text = "010800003601200021588448654665391EE0692QKT9vdPhgmoRg6GAKmYgpMiP6X8HYolEeukFLhrQBfo"
    assert any(
        map(lambda datamatrix: decode_text in datamatrix[0].decode(), list_datamatrix)
    )


@pytest.mark.skip
def test_datamatrix_convector_hard_images():
    path_to_image = os.path.join("example", "datamatrix.png")
    list_datamatrix = decode_image(cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED))
    decode_text = "010460180800004721DpNcisy6vCERY91EE0692SPAXkDQJdS4VIj+rtATpWbOF8u0mdHdDJyaOJb2avNQ="
    assert any(
        map(lambda datamatrix: decode_text in datamatrix[0].decode(), list_datamatrix)
    )
@pytest.mark.skip
def test_datamatrix_convector_no_crop_images():
    path_to_image = os.path.join("example", "tantum_matrix.jpeg")
    list_datamatrix = decode_image(cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED))
    decode_text = "010800003601200021588448654665391EE0692QKT9vdPhgmoRg6GAKmYgpMiP6X8HYolEeukFLhrQBfo"
    assert any(
        map(lambda datamatrix: decode_text in datamatrix[0].decode(), list_datamatrix)
    )


def test_get_medicine_from_datamatrix():
    datamatrix_text = "010460180800004721DpNcisy6vCERY91EE0692SPAXkDQJdS4VIj+rtATpWbOF8u0mdHdDJyaOJb2avNQ="
    medicine = Medicine(name="Ревит", mnn="поливитамины" )

