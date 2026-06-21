# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00935(request):
    upload_name = request.FILES['doc'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
