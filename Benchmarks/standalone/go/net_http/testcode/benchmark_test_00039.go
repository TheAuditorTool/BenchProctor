// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00039(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	if authHeader != "" {
		data = authHeader
	}
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		http.Error(w, "malformed order", http.StatusBadRequest)
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	orderTotal := totalNode.InnerText()
	RespondJSON(w, http.StatusOK, map[string]string{"total": orderTotal})
}
