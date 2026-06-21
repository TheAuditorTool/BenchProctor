# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def relay_value(value):
    return value

def BenchmarkTest20212(request):
    user_id = request.GET.get('id', '')
    data = relay_value(user_id)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
