// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"strings"
)

func BenchmarkTest00199(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
