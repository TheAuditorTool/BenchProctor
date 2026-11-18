// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"
)

func BenchmarkTest00488(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	relayPrefix := ""
	if len(graphqlVar) > 0 {
		relayPrefix = strings.ToLower(graphqlVar[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = graphqlVar
	case "f":
		data = graphqlVar
	default:
		data = graphqlVar
	}
	http.Redirect(w, r, data, http.StatusFound)
}
