# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51674(request):
    stdin_value = input('input: ')
    data = ' '.join(str(stdin_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
