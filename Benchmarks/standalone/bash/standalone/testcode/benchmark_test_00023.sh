#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00023() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  printf '%s' "$data" | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00023 "$@"
