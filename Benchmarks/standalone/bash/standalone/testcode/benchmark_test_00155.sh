#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00155() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  echo -n "$user_input" | md5sum
}

benchmark_test_00155 "$@"
