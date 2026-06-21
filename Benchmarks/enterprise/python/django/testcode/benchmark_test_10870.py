# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def BenchmarkTest10870(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
