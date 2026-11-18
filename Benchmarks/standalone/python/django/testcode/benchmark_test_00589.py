# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00589(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
