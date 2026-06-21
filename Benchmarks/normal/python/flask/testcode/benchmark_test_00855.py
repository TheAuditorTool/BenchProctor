# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest00855():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    return Markup('<img src="' + str(data) + '">')
