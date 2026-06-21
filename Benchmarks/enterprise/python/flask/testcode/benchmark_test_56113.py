# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest56113():
    upload_name = request.files['upload'].filename
    entries = os.listdir(str(upload_name))
    return jsonify({'listing': entries}), 200
