# SPDX-License-Identifier: Apache-2.0
import bleach
from django.http import HttpResponse


def BenchmarkTest00089(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % str(header_value)
    processed = bleach.clean(data)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(processed) + '</div>')
    return resp
