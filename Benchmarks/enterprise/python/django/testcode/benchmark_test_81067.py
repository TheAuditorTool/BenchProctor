# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest81067(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
