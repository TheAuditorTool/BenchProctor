# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest63187(request):
    user_id = request.GET.get('id', '')
    if re.search('[a-zA-Z0-9_-]+', str(user_id)):
        return JsonResponse({'validated': str(user_id)}, status=200)
    return JsonResponse({"saved": True})
