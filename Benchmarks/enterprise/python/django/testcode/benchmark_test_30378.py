# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def BenchmarkTest30378(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    return HttpResponse(mark_safe('<img src="' + str(json_value) + '">'))
