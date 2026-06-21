# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest10078(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
