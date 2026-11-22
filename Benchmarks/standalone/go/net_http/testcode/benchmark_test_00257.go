// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"net/http"
)

func BenchmarkTest00257(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(jsonValue)
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
