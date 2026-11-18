# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00267(request, path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
