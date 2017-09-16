import tempfile
import zipfile

import shutil

from dataset.dicom_reader import read_dicom


def filter_dicom(files):
    return filter(lambda filename: filename.endswith('.dcm'), files)


def read_sunnybrook_images(path):
    with zipfile.ZipFile(path, 'r') as zip_file:
        for filename in filter_dicom(zip_file.namelist()):
            print(filename)

            with tempfile.NamedTemporaryFile('wb') as temp_dicom:
                with zip_file.open(filename, 'r') as zipped_dicom:
                    shutil.copyfileobj(zipped_dicom, temp_dicom.file)
                read_dicom(temp_dicom.name)

