# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71992(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
