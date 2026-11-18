# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00172(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
