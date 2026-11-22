#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00035() {
  user_input="`cat /dev/stdin`"
  data=`printf "%b" "$user_input"`
  printf '%s' "$data" | xmllint --nonet --dropdtd - | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00035 "$@"
