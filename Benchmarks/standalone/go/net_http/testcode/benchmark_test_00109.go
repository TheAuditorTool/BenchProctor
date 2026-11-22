// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00109(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	segments := strings.Split(rawBody, ",")
	data := strings.Join(segments, " ")
	trustedSettings.Store("partner_callback_host", data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
