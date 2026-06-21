# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06207(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
