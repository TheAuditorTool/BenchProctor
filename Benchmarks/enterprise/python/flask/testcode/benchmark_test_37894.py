# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest37894():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
