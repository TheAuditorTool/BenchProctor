# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest09360(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = normalise_input(forwarded_ip)
    processed = data[:64]
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
