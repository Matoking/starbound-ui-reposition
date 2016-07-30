import glob
import os
import io

import zipfile

from jinja2 import Template


def get_files():
    """Get a dict containing all files to be packed into the ZIP"""
    files = {}
    current_path = os.path.dirname(os.path.abspath(__file__))

    for root, dirnames, filenames in os.walk("%s/data" % current_path):
        for filename in filenames:
            content = None
            file_path = os.path.join(root, filename)

            with open(file_path, 'rb') as f:
                content = f.read()

            # Turn the absolute path into a relative path
            file_path = file_path.replace(current_path, "")
            file_path = file_path.replace("/data/", "")
            file_path = os.path.join("hud_repositioning", file_path)
            files[file_path] = content

    return files


def patch_files(files, parameters):
    """
    Patch the .patch files to have correct values per values provided
    in parameters
    """
    for file_name in files.keys():
        if file_name.endswith(".patch"):
            content = files[file_name]

            template = Template(content)
            result = template.render({
                "TOP": parameters["top"],
                "BOTTOM": parameters["bottom"],
                "LEFT": parameters["left"],
                "RIGHT": parameters["right"]
            })

            files[file_name] = result

    return files


def create_zip(files):
    """
    Write all given files in a dict to a ZIP file and return it as raw data
    """
    byte_file = io.BytesIO()
    zip_file = zipfile.ZipFile(byte_file, 'w', zipfile.ZIP_DEFLATED)

    for file_name, file_data in files.iteritems():
        zip_file.writestr(file_name, file_data)

    zip_file.close()
    return byte_file.getvalue()


def create_mod(parameters):
    """Create a Starbound mod and return it as ZIP data"""
    files = get_files()
    files = patch_files(files, parameters)

    zip_data = create_zip(files)

    return zip_data
