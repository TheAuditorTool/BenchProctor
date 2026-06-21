# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest54651(request):
    host_value = request.META.get('HTTP_HOST', '')
    return HttpResponse(str(host_value), content_type='text/html')
