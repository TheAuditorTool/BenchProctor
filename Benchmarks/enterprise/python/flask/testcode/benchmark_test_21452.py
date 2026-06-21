# SPDX-License-Identifier: Apache-2.0
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest21452(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
