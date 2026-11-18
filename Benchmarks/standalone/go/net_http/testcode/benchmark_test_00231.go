// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00231(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", userID)
	data := relayBuilder.String()
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	RespondJSON(w, http.StatusOK, map[string]string{"name": *result})
}
