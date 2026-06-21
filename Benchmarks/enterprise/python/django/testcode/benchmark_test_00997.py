# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00997(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
