// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net"
	"net/http"
	"strings"
)

func BenchmarkTest00406(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var data string
	for _, token := range strings.Split(graphqlVar, ",") {
		data = token
	}
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
