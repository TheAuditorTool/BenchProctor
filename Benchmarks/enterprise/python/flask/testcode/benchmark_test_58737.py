# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest58737():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return Markup('<div>' + str(data) + '</div>')
