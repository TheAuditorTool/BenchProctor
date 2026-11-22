// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net"
	"net/http"
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00258(c *gin.Context) {
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
		c.String(http.StatusBadRequest, "invalid url")
		return
	}
	conn, err := net.Dial("tcp", net.JoinHostPort(dialURL.Hostname(), "80"))
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
