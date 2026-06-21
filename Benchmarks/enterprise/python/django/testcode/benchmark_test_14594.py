# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import csv
import io


def BenchmarkTest14594(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    cell = str(data)
    if cell[:1] in ('=', '+', '-', '@', '\t', '\r'):
        cell = "'" + cell
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)
    writer.writerow([cell])
    return JsonResponse({"saved": True})
