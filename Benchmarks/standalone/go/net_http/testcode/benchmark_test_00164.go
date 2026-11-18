// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00164(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	var data string
	for _, token := range strings.Split(userID, ",") {
		data = token
	}
	os.Remove("/var/app/data/" + data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
