// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net"
	"net/http"
)

func BenchmarkTest00102(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	form := submissionForm{payload: rawBody}
	data := form.payload
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
