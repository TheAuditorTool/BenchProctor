# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import ctypes


def BenchmarkTest03153(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
