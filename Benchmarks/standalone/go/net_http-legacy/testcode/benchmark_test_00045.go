// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
)

func BenchmarkTest00045(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	const unitPriceCents int32 = 129999
	quantity, err := strconv.ParseInt(cookieValue, 10, 32)
	if err != nil {
		http.Error(w, "invalid quantity", http.StatusBadRequest)
		return
	}
	lineTotal := int32(quantity) * unitPriceCents
	DB.Exec("INSERT INTO invoice_lines (sku, qty, total_cents) VALUES ($1, $2, $3)", "SKU-4410", quantity, lineTotal)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
