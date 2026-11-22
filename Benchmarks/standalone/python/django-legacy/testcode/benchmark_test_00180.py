# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00180(request):
    field_value = request.POST.get('field', '')
    data = f'{field_value!s}'
    request.session.update({'data': str(data)})
    return JsonResponse({"saved": True})
