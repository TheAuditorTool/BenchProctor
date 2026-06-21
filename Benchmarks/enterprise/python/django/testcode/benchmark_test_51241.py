# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest51241(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
