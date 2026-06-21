# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest55141(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
