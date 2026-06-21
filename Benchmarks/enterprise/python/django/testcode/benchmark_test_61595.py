# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest61595(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    return HttpResponse('<script src="' + str(origin_value) + '"></script>', content_type='text/html')
