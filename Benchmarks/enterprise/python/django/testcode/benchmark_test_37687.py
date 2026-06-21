# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest37687(request):
    user_id = request.GET.get('id', '')
    if user_id not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = user_id
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
