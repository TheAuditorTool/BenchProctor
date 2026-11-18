# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def BenchmarkTest00152(request):
    field_value = request.POST.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
