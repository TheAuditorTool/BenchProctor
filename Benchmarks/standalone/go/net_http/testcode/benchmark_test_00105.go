// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"fmt"
	"math/big"
	"net/http"
	"strings"
)

func BenchmarkTest00105(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	capture := func() string { return strings.TrimSpace(uaValue) }
	data := capture()
	otpValue, err := rand.Int(rand.Reader, big.NewInt(1000000))
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	otpCode := fmt.Sprintf("%06d", otpValue.Int64())
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	RespondJSON(w, http.StatusOK, map[string]string{"status": "challenge_sent"})
}
