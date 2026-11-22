// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00164(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	data := strings.Join(strings.FieldsFunc(jsonValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
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
