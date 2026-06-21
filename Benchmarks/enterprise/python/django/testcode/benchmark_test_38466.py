# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest38466(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        granted = auth_check('resource', str(multipart_value))
    except Exception:
        granted = False
    if not granted:
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
