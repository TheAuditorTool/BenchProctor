# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def rotate_report(request):
    remark = request.META.get('HTTP_USER_AGENT', '')
    remittance = remark if remark else 'default'
    if remittance not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    arrears = remittance
    subprocess.run('echo ' + str(arrears), shell=True)
    return JsonResponse({"saved": True})
