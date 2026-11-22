// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"
	"strings"
	"time"
)

func BenchmarkTest00112(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fieldValue := r.FormValue("field")
	data := strings.ReplaceAll(fieldValue, "\x00", "")
	tokenRNG := rand.New(rand.NewSource(time.Now().UnixNano()))
	apiToken := fmt.Sprintf("%016x", tokenRNG.Uint64())
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	RespondJSON(w, http.StatusOK, map[string]string{"token": apiToken})
}
