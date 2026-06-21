# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30911(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
