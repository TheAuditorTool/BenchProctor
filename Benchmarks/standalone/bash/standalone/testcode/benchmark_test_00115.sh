#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00115() {
  dd if=/dev/urandom bs=16 count=1 2>/dev/null | xxd -p
}

benchmark_test_00115 "$@"
