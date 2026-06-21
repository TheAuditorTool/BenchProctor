# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest35284(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
