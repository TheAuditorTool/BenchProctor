// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00015(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(dbValue)
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		http.Error(w, "malformed order", http.StatusBadRequest)
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	if totalNode == nil {
		http.Error(w, "order total missing", http.StatusBadRequest)
		return
	}
	orderTotal := totalNode.InnerText()
	RespondJSON(w, http.StatusOK, map[string]string{"total": orderTotal})
}
