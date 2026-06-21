# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from flask import request


def BenchmarkTest64673():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
