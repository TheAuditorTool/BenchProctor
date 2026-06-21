# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest04114(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
