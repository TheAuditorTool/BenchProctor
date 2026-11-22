#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00155() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  printf '%s' "$data" | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00155 "$@"
