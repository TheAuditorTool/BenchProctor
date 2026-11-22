#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00097() {
  user_input="$USER_COMMENT"
  printf -v data "%s" "${user_input}"
  printf '%s' "$data" | xmllint --nonet --dropdtd - | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00097 "$@"
