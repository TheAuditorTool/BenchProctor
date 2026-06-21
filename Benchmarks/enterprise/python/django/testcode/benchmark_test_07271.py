# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest07271(request):
    user_id = request.GET.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
