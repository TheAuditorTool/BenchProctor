# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest00108(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
