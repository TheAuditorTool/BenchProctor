# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest05487(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    return HttpResponse(str(origin_value), content_type='text/html')
