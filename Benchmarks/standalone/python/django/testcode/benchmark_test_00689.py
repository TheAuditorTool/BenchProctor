# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00689(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
