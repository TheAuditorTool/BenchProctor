# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00623(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
