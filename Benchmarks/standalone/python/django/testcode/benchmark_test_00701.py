# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest00701(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = str(forwarded_ip).split(',')
    data = ' '.join(parts)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
