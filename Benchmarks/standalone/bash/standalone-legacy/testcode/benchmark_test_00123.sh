#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00123() {
  user_input="$USER_COMMENT"
  if _parsed=`printf "%d" "${user_input}" 2>/dev/null`; then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  printf '%s' "$data" | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00123 "$@"
