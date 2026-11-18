// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"strings"
)

func BenchmarkTest00079(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	data := strings.ReplaceAll(multipartValue, "\x00", "")
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
