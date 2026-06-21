# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest11176(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(json_value) + ' -->', content_type='text/html')
