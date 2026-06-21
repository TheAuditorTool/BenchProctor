# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52939(request):
    upload_name = request.FILES['doc'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
