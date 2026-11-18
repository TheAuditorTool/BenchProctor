// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"
)

func BenchmarkTest00061(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	pending := strings.Split(jsonValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
