# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest55848():
    xml_value = request.get_data(as_text=True)
    os.environ['APP_USER_PREFERENCE'] = str(xml_value)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
