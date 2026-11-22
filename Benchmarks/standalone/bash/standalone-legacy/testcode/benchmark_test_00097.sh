#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00097() {
  user_input="`cat /dev/stdin`"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=`normalize "$user_input"`
  printf '%s' "$data" | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00097 "$@"
