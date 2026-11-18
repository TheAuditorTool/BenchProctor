# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00255(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
