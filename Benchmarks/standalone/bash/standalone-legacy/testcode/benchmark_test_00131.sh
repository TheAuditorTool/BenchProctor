#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00131() {
  user_input="`sed -n '/^\r*$/{n;s/\r$//;p;q}'`"
  data=`printf "%s" "$user_input"`
  printf '%s' "$data" | xmllint --nonet --dropdtd - | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00131 "$@"
