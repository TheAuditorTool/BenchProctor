// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"io"
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00111(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(rawBody), &parsed)
	data, _ := parsed["value"].(string)
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		http.Error(w, "malformed order", http.StatusBadRequest)
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	orderTotal := totalNode.InnerText()
	RespondJSON(w, http.StatusOK, map[string]string{"total": orderTotal})
}
