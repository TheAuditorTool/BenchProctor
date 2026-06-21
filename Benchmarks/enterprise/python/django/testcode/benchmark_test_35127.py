# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def BenchmarkTest35127(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
