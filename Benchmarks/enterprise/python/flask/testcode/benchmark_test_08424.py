# SPDX-License-Identifier: Apache-2.0
import unicodedata


def BenchmarkTest08424(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
