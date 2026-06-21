# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21493(request):
    stdin_value = input('input: ')
    with open('/var/app/data/' + str(stdin_value), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
