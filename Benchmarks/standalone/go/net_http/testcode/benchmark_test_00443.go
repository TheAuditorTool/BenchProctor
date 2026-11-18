// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"
)

func BenchmarkTest00443(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := func(v string) string { return strings.TrimSpace(v) }(graphqlVar)
	http.Redirect(w, r, data, http.StatusFound)
}
