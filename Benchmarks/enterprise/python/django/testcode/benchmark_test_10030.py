# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io
import json


def relay_value(value):
    return value

def BenchmarkTest10030(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
