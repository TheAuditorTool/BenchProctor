// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
)

func BenchmarkTest00035(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(graphqlVar)
	http.Redirect(w, r, data, http.StatusFound)
}
