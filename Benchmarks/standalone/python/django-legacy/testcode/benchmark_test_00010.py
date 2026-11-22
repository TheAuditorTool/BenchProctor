# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00010(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ' '.join(parts)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
