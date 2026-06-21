# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest07420(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = FormData(payload=auth_header).payload
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
