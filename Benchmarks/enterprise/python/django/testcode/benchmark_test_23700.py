# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest23700(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = normalise_input(referer_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
