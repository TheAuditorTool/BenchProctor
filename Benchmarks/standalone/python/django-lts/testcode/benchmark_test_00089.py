# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00089(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(data) + '</div>')
    return resp
