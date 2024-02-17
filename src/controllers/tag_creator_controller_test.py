from unittest.mock import patch
from src.drivers.barcode_handler import BarCodeHandler
from .tag_creator_controller import TagCreatorController

@patch.object(BarCodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = "image_path"
    mock_create_barcode.return_value =  mock_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)
    print(result)
