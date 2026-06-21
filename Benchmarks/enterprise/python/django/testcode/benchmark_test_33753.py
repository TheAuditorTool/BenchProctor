# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest33753(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ensure_str(json_value)
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
