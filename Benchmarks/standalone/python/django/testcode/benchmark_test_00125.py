# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00125(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ' '.join(parts)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
