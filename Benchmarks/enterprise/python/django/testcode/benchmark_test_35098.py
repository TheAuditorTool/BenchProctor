# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import auth_check


def BenchmarkTest35098(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    if data != request.session.get('csrf_token'):
        return JsonResponse({'error': 'CSRF token mismatch'}, status=403)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
