// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00045(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(headerValue)
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	conn, err := net.Dial("tcp", targetUrl)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
