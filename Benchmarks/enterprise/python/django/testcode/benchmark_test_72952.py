# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest72952(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
