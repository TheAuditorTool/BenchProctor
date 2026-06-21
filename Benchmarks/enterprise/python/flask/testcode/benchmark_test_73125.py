# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import jsonify


def BenchmarkTest73125(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return '<script src="' + str(target_url) + '"></script>', 200, {'Content-Type': 'text/html'}
