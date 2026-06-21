# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from django.http import HttpResponse


def BenchmarkTest62910(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
