// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00155(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := strings.Join(strings.FieldsFunc(dbValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		http.Error(w, "malformed order", http.StatusBadRequest)
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	orderTotal := totalNode.InnerText()
	RespondJSON(w, http.StatusOK, map[string]string{"total": orderTotal})
}
