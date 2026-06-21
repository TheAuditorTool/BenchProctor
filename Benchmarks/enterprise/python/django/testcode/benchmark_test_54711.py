# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54711(request):
    upload_name = request.FILES['upload'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
