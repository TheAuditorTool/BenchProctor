# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11829(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
