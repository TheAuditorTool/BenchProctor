// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"io"
	"net/http"
)

func BenchmarkTest00159(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(rawBody), &parsed)
	data, _ := parsed["value"].(string)
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
