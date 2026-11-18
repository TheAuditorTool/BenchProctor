// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
)

func BenchmarkTest00154(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	if authHeader != "" {
		data = authHeader
	}
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
