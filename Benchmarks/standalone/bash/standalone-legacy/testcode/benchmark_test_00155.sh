#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00155() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  data="${user_input:-default}"
  printf '%s' "$data" | xmllint --nonet --dropdtd - | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00155 "$@"
