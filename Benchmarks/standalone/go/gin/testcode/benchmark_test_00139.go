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

func BenchmarkTest00139(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	relayPrefix := ""
	if len(headerValue) > 0 {
		relayPrefix = strings.ToLower(headerValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = headerValue
	case "f":
		data = headerValue
	default:
		data = headerValue
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
