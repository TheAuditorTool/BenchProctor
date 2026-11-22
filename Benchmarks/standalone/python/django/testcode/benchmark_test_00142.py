# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00142(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
