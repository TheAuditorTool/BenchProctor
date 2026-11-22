// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
)

func BenchmarkTest00146(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := fmt.Sprintf("%s", headerValue)
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		http.Error(w, "invalid integer", http.StatusBadRequest)
		return
	}
	boundedVal := strconv.Itoa(max(0, min(_num, 2147483647)))
	const unitPriceCents int32 = 129999
	quantity, err := strconv.ParseInt(boundedVal, 10, 32)
	if err != nil {
		http.Error(w, "invalid quantity", http.StatusBadRequest)
		return
	}
	lineTotal := int64(quantity) * int64(unitPriceCents)
	DB.Exec("INSERT INTO invoice_lines (sku, qty, total_cents) VALUES ($1, $2, $3)", "SKU-4410", quantity, lineTotal)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
