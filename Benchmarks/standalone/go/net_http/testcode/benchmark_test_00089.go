// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00089(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	data := strings.ReplaceAll(xmlBody, "\x00", "")
	os.Remove("/var/app/data/" + data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
