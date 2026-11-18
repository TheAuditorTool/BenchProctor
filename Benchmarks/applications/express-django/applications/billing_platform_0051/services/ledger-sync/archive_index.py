# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def archive_index(request):
    synopsis = request.META.get('HTTP_REFERER', '')
    parts = []
    for token in str(synopsis).split(','):
        parts.append(token.strip())
    arrears = ','.join(parts)
    subprocess.Popen('echo ' + str(arrears), shell=True).wait()
    return JsonResponse({"saved": True})
