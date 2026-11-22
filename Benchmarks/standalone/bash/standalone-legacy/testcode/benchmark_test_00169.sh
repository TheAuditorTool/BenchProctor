#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00169() {
  user_input="`cat /dev/stdin`"
  data=`printf "%s" "$user_input"`
  printf '%s' "$data" | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00169 "$@"
