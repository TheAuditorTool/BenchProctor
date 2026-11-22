// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00104(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	pending := strings.Split(authHeader, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	trustedSettings.Store("partner_callback_host", data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
