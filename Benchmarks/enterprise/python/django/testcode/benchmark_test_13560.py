# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest13560(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
