// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00110(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fieldValue := r.FormValue("field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", fieldValue)
	data := relayBuilder.String()
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		http.Error(w, "invalid id", http.StatusBadRequest)
		return
	}
	parsedId := strconv.Itoa(_num)
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users WHERE id = ?", parsedId).Scan(&matched).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
