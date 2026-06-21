# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09679(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
