// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"
)

func BenchmarkTest00082(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	uaValue := r.Header.Get("User-Agent")
	otpValue := rand.Int31n(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", uaValue, otpCode)
	RespondJSON(w, http.StatusOK, map[string]string{"status": "challenge_sent"})
}
