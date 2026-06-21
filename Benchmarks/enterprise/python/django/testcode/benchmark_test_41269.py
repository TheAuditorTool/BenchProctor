# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest41269(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
