# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest45729(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
