# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import ast


def BenchmarkTest36096(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
