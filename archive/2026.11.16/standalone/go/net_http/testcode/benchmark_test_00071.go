// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00071(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	data := func(v string) string { return strings.TrimSpace(v) }(forwardedIP)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
