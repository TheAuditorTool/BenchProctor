# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest74693(request):
    upload_name = request.FILES['upload'].name
    processed = 'true' if str(upload_name).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HttpResponse(Template(processed).render(Context()))
