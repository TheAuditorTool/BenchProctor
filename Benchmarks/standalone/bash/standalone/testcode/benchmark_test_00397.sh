#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00397() {
  user_input="$(cat /dev/stdin)"
  checked_path="/var/app/data/$(basename -- "$user_input")"
  cat "$checked_path"
}

benchmark_test_00397 "$@"
