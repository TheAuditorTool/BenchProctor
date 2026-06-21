# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58891(request):
    upload_name = request.FILES['upload'].name
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(upload_name))
    return JsonResponse({"saved": True})
