# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest78698(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
