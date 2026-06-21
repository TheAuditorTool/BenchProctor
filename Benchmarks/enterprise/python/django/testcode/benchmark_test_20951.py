# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20951(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
