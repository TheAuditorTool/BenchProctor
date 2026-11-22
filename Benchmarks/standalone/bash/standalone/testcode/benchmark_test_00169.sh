#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00169() {
  user_input="$(cat /dev/stdin)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  printf '%s' "$data" | xmllint --nonet --dropdtd - | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00169 "$@"
