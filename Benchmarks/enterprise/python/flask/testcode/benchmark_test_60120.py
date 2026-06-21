# SPDX-License-Identifier: Apache-2.0
import unicodedata


def BenchmarkTest60120(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
