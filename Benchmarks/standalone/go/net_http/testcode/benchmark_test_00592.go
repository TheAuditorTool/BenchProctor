// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00592(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", graphqlVar)
	data := relayBuilder.String()
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
