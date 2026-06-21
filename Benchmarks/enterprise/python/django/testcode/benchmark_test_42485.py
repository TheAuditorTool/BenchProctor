# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest42485(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    return HttpResponse(str(data), content_type='text/html')
