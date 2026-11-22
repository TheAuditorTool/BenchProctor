// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net"
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00061(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := ioutil.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	var data string
	for _, token := range strings.Split(apiValue, ",") {
		data = token
	}
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
