# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11593(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
