# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest15719(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
