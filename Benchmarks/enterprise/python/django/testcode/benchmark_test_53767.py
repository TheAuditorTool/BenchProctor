# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest53767(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
