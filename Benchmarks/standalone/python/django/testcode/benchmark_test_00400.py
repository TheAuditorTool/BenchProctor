# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00400(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
