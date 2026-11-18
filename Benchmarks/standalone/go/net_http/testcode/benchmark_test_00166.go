// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"net"
	"net/http"
)

func BenchmarkTest00166(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	decodedBytes, _ := base64.StdEncoding.DecodeString(cookieValue)
	data := string(decodedBytes)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
