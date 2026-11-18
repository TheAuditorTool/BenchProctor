// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/json"
	"net/http"
	"strings"
)

func BenchmarkTest00022(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	data := strings.ReplaceAll(jsonValue, "\x00", "")
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
