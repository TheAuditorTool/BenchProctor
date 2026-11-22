// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net"
	"net/http"
	"net/url"
)

func BenchmarkTest00044(w http.ResponseWriter, r *http.Request) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	form := submissionForm{payload: redisValue}
	data := form.payload
	dialURL, dialErr := url.Parse(data)
	if dialErr != nil {
		http.Error(w, "invalid url", http.StatusBadRequest)
		return
	}
	conn, err := net.Dial("tcp", net.JoinHostPort(dialURL.Hostname(), "80"))
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
