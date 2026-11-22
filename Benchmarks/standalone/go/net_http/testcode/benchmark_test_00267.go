// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00267(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := fieldValue
	if _, after, ok := strings.Cut(fieldValue, ","); ok {
		data = after
	}
	const unitPriceCents int32 = 129999
	quantity, err := strconv.ParseInt(data, 10, 32)
	if err != nil {
		http.Error(w, "invalid quantity", http.StatusBadRequest)
		return
	}
	lineTotal := int32(quantity) * unitPriceCents
	DB.Exec("INSERT INTO invoice_lines (sku, qty, total_cents) VALUES ($1, $2, $3)", "SKU-4410", quantity, lineTotal)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
