# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00349(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    with open('/var/app/data/' + str(forwarded_ip), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
