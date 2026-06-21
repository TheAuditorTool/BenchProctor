# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import os
import ast


def BenchmarkTest03710(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    return JsonResponse({"saved": True})
