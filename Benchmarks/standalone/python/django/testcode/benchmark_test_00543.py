# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00543(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ' '.join(parts)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
