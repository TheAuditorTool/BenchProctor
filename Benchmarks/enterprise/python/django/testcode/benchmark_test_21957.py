# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21957(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
