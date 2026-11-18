// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00555(w http.ResponseWriter, r *http.Request) {
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := io.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(apiValue)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
