# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63309(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
