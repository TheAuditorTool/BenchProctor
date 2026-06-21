# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52226(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
