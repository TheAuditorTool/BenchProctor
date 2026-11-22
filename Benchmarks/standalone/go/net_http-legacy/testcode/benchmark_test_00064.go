// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"
	"strings"
)

func BenchmarkTest00064(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	data := func(v string) string { return strings.TrimSpace(v) }(cookieValue)
	otpValue := rand.Int31n(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	RespondJSON(w, http.StatusOK, map[string]string{"status": "challenge_sent"})
}
