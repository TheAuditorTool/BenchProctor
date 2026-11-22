// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"fmt"
	"math/big"
	"net/http"
	"strings"
)

func BenchmarkTest00184(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	data := fmt.Sprintf("%s", pathValue)
	otpValue, err := rand.Int(rand.Reader, big.NewInt(1000000))
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	otpCode := fmt.Sprintf("%06d", otpValue.Int64())
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	RespondJSON(w, http.StatusOK, map[string]string{"status": "challenge_sent"})
}
