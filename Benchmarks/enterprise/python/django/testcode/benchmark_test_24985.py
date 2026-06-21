# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest24985(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
