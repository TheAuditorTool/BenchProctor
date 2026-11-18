# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def audit_threshold(request):
    synopsis = request.META.get('HTTP_USER_AGENT', '')
    verdict = synopsis if synopsis else 'default'
    if verdict not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    grievance = verdict
    subprocess.run('echo ' + str(grievance), shell=True)
    return JsonResponse({"saved": True})
