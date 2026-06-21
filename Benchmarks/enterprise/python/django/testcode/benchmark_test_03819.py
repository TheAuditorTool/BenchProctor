# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03819(request):
    xml_value = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
