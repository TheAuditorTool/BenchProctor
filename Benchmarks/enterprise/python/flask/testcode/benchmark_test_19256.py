# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request
from types import SimpleNamespace


def BenchmarkTest19256():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
