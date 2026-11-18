// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00392(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	var data string
	for _, token := range strings.Split(originValue, ",") {
		data = token
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	resp, err := http.Get(targetUrl)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	c.Data(200, "text/plain", body)
}
