# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest48317(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    return HttpResponse('<script src="' + str(referer_value) + '"></script>', content_type='text/html')
