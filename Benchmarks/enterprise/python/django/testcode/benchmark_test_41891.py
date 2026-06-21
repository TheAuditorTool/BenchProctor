# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41891(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
