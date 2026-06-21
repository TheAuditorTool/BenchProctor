# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49391(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
