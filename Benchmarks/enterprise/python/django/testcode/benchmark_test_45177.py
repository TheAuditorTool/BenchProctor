# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import json
import urllib.parse


def BenchmarkTest45177(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % (json_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
