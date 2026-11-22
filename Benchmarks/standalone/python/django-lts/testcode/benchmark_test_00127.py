# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00127(request):
    field_value = request.POST.get('field', '')
    parts = str(field_value).split(',')
    data = ' '.join(parts)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(data) + '</div>')
    return resp
