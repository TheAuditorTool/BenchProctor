// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00148(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	refererValue := r.Header.Get("Referer")
	var data string
	if len(refererValue) > 0 {
		data = refererValue
	} else {
		data = "default"
	}
	trustedSettings.Store("partner_callback_host", data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
