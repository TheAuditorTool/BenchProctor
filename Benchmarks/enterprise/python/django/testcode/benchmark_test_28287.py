# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest28287(request):
    user_id = request.GET.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
