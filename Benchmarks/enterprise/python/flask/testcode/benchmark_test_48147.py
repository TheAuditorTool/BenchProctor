# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
import unicodedata


def BenchmarkTest48147(path_param):
    path_value = path_param
    data = unquote(path_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
