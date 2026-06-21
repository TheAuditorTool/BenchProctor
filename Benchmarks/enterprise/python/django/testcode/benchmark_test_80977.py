# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80977(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
