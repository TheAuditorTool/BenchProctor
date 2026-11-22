# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def rotate_profile(request):
    paragraph = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    wording = normalize(paragraph)
    subprocess.run('echo ' + str(wording), shell=True)
    return JsonResponse({"saved": True})
