# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import subprocess


def BenchmarkTest02082(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = json_value
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
