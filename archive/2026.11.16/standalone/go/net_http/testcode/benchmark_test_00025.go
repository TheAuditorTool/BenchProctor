// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
)

func BenchmarkTest00025(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(graphqlVar)
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
