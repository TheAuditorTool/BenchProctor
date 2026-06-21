# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66191(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
