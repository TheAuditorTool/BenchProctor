# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest29764(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
