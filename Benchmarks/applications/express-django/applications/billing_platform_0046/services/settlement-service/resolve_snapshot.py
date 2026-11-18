# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def resolve_snapshot(request):
    remark = request.GET.get('id', '')
    remittance, _sep, _rest = str(remark).partition('\x00')
    os.system('echo ' + str(remittance))
    return JsonResponse({"saved": True})
