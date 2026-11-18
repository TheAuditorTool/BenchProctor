// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net"
	"net/http"
)

func BenchmarkTest00356(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := fmt.Sprintf("%s", refererValue)
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
