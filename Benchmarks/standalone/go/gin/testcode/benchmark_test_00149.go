// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00149(c *gin.Context) {
	fieldValue := c.PostForm("field")
	relayPrefix := ""
	if len(fieldValue) > 0 {
		relayPrefix = strings.ToLower(fieldValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = fieldValue
	case "f":
		data = fieldValue
	default:
		data = fieldValue
	}
	parsedURL, parseErr := url.Parse(data)
	if parseErr != nil || (parsedURL.Scheme != "http" && parsedURL.Scheme != "https") || parsedURL.User != nil || strings.ContainsAny(data, "\\ \t\r\n") || !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	c.Redirect(http.StatusFound, targetUrl)
}
