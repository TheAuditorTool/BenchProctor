// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
)

func BenchmarkTest00136(w http.ResponseWriter, r *http.Request) {
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
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
