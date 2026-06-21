# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63898(request, path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
