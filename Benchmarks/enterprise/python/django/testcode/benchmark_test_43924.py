# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43924(request):
    stdin_value = input('input: ')
    pending = list(str(stdin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
