# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest78061():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    return Markup('<img src="' + str(data) + '">')
