# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re
import json


def BenchmarkTest66143(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = json_value
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
