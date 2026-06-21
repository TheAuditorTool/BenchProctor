# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from urllib.parse import unquote


def BenchmarkTest24981(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
