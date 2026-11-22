# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00033(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    code = compile(str(data), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
