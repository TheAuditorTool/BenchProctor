#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00138() {
  reset_code=`openssl rand -hex 16`
  echo "$reset_code"
}

benchmark_test_00138 "$@"
