# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30600(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
