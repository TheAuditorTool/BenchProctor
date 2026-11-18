#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00221() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden" >&2; exit 1; fi
  cat "$checked_path"
}

benchmark_test_00221 "$@"
