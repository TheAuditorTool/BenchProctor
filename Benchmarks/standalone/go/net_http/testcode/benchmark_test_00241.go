// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha3"
	"encoding/hex"
	"encoding/json"
	"net/http"
	"strings"
)

func BenchmarkTest00241(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := strings.ReplaceAll(graphqlVar, "\x00", "")
	strongDigest := sha3.New256()
	strongDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(strongDigest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
