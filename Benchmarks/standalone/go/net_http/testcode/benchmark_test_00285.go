// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strconv"
)

func BenchmarkTest00285(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(graphqlVar)
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
