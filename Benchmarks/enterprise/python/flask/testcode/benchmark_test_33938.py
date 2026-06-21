# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest33938():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
