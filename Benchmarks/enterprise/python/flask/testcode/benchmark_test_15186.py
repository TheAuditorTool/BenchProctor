# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest15186():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
