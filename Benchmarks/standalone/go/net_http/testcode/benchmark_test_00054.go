// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"net/url"
)

func BenchmarkTest00054(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	w.Header().Add("Set-Cookie", "session=" + url.QueryEscape(graphqlVar) + "; Path=/; HttpOnly; SameSite=Strict")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
