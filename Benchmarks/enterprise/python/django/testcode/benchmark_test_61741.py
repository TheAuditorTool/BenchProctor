# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61741(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
