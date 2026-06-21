# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
import subprocess


def BenchmarkTest30687(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
