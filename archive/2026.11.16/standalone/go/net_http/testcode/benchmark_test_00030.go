// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
)

func BenchmarkTest00030(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := fmt.Sprintf("%s", graphqlVar)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
