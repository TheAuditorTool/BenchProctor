# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest38231(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
