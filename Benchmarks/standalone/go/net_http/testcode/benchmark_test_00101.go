// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"net/http"
)

func BenchmarkTest00101(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var data string
	if len(graphqlVar) > 0 {
		data = graphqlVar
	} else {
		data = "default"
	}
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
