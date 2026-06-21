# SPDX-License-Identifier: Apache-2.0
import os
from flask import request
from types import SimpleNamespace


def BenchmarkTest07831():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
