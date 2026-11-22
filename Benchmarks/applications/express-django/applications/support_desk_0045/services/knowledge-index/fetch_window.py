# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def fetch_window(request):
    remark = request.POST.get('field', '')
    inquiry = (lambda v: v.strip())(remark)
    if inquiry not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    grievance = inquiry
    os.system('echo ' + str(grievance))
    return JsonResponse({"saved": True})
