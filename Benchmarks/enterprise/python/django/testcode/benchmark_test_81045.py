# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81045(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
