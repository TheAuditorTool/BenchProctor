#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00045() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  data="${user_input//$'\x00'/}"
  checked_path="/var/app/data/$(basename -- "$data")"
  cat "$checked_path"
}

benchmark_test_00045 "$@"
