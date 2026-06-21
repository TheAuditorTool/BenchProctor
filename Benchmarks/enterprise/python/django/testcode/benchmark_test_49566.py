# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49566(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % (forwarded_ip,)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
