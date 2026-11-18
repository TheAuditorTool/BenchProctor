// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00389(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := func(v string) string { return strings.TrimSpace(v) }(headerValue)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
