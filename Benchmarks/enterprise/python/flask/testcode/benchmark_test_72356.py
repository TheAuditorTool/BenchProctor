# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest72356(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    return Markup('<img src="' + str(data) + '">')
