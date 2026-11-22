# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00109(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name!s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
