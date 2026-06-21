# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import sys


def BenchmarkTest65286(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
