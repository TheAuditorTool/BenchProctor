// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"
)

func BenchmarkTest00223(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	capture := func() string { return strings.TrimSpace(jsonValue) }
	data := capture()
	trustedSettings.Store("partner_callback_host", data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
