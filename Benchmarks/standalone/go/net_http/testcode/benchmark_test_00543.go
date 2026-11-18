// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00543(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	segments := strings.Split(graphqlVar, ",")
	data := strings.Join(segments, " ")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
