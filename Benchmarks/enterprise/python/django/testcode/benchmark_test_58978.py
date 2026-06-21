# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest58978(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
