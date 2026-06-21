# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19934(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
