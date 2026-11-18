// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00006(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(jsonValue)
	resp, err := http.Get(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	w.Write(body)
}
