# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest36362(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
