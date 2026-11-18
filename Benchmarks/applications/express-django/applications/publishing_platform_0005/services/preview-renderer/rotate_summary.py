# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def rotate_summary(request):
    footnote = request.META.get('HTTP_USER_AGENT', '')
    byline = footnote if footnote else 'default'
    if byline not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    addendum = byline
    subprocess.run('echo ' + str(addendum), shell=True)
    return JsonResponse({"saved": True})
