// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00179(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	relayPrefix := ""
	if len(pathValue) > 0 {
		relayPrefix = strings.ToLower(pathValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = pathValue
	case "f":
		data = pathValue
	default:
		data = pathValue
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
