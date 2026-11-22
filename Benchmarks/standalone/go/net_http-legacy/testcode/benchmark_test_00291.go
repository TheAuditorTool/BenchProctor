// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"
)

func BenchmarkTest00291(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	val := rand.Intn(1000000)
	RespondJSON(w, http.StatusOK, map[string]string{"token": fmt.Sprintf("%d", val)})
}
