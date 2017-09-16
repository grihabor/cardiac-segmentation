import os
import itertools
import logging
import tempfile
import zipfile

import shutil

from dataset.dicom_reader import read_dicom


logger = logging.getLogger(__name__)


def filter_dicom(files):
    return itertools.islice(
        filter(lambda filename: filename.endswith('.dcm'), files),
        5
    )


def clean_cache():
    root_path = '/data/cache'
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            path = os.path.join(root_path, filename)
            try:
                os.remove(path)
            except FileNotFoundError as e:
                logger.warning(e)


def read_sunnybrook_images(path):
    clean_cache()

    with zipfile.ZipFile(path, 'r') as zip_file:
        for filename in filter_dicom(zip_file.namelist()):
            print(filename)

            with tempfile.NamedTemporaryFile('wb') as temp_dicom:
                with zip_file.open(filename, 'r') as zipped_dicom:
                    shutil.copyfileobj(zipped_dicom, temp_dicom.file)
                read_dicom(temp_dicom.name)

