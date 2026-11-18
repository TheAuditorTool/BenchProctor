# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def BenchmarkTest00636(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
