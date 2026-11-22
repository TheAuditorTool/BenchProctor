// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00139(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", originValue)
	data := relayBuilder.String()
	parsedURL, parseErr := url.Parse(data)
	if parseErr != nil || (parsedURL.Scheme != "http" && parsedURL.Scheme != "https") || parsedURL.User != nil || strings.ContainsAny(data, "\\ \t\r\n") || !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	c.Header("Location", targetUrl)
	c.Status(http.StatusSeeOther)
}
