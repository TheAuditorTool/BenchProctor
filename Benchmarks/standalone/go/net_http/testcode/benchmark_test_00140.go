// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"fmt"
	"math/big"
	"net/http"
)

func BenchmarkTest00140(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(multipartValue)
	otpValue, err := rand.Int(rand.Reader, big.NewInt(1000000))
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	otpCode := fmt.Sprintf("%06d", otpValue.Int64())
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	RespondJSON(w, http.StatusOK, map[string]string{"status": "challenge_sent"})
}
