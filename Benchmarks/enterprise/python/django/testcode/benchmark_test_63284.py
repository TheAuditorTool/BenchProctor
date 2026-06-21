# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63284(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
