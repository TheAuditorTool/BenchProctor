# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00181(request):
    field_value = request.POST.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
