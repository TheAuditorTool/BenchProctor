// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"encoding/json"
	"fmt"
	"net/http"
)

func BenchmarkTest00057(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	form := submissionForm{payload: graphqlVar}
	data := form.payload
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
