import logging

import pytest

from classification_model.config.core import config
from classification_model.processing.data_manager import load_dataset

logger = logging.getLogger(__name__)


@pytest.fixture
def sample_input_data():
    data = load_dataset(file_name=config.app_config.test_data_file)

    return data
