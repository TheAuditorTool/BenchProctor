# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest11635(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    return HttpResponse(str(data), content_type='text/html')
