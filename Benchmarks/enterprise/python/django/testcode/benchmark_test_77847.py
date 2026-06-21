# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest77847(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
