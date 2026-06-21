# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest11634(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    return HttpResponse(Template(data).render(Context()))
