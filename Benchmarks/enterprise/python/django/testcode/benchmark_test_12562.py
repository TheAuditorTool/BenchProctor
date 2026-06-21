# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from django.http import HttpResponse


def BenchmarkTest12562(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json.loads(json_value).get('value', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
