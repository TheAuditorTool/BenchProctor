# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def collect_threshold(request, path_param):
    remark = request.path.split('/')[-1]
    note = f'{remark!s}'
    os.unlink('/var/app/data/' + str(note))
    return JsonResponse({"saved": True})
