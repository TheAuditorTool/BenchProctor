# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import os
import ast


def BenchmarkTest30699(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return JsonResponse({"saved": True})
