# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70026(request):
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
