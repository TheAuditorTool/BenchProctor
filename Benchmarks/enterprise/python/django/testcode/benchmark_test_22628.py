# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest22628(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
