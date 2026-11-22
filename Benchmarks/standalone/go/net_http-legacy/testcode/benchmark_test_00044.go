// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io/ioutil"
	"net/http"
	"strings"
)

func BenchmarkTest00044(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := func(v string) string { return strings.TrimSpace(v) }(redisValue)
	resp, err := http.Get(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)
	w.Write(body)
}
