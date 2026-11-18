// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00292(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	capture := func() string { return strings.TrimSpace(refererValue) }
	data := capture()
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		http.Error(w, "invalid id", http.StatusBadRequest)
		return
	}
	parsedId := strconv.Itoa(_num)
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", parsedId)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
