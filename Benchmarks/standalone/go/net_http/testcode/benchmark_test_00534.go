// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00534(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := hostValue
	if _, after, ok := strings.Cut(hostValue, ","); ok {
		data = after
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
