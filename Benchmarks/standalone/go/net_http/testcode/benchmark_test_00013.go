// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
)

func BenchmarkTest00013(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	http.Redirect(w, r, graphqlVar, http.StatusFound)
}
