# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest72607(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
