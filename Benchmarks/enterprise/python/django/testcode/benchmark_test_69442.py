# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69442(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
