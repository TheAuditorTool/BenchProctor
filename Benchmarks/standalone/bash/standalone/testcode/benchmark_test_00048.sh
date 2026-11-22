#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00048() {
  user_input="$(cat /dev/stdin)"
  data="${user_input:-default}"
  printf '%s' "$data" | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00048 "$@"
