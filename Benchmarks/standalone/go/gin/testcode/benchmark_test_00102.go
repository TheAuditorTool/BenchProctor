// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00102(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := strings.Join(strings.FieldsFunc(refererValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	parsedURL, parseErr := url.Parse(data)
	if parseErr != nil || (parsedURL.Scheme != "http" && parsedURL.Scheme != "https") || parsedURL.User != nil || strings.ContainsAny(data, "\\ \t\r\n") || !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	http.RedirectHandler(targetUrl, http.StatusFound).ServeHTTP(c.Writer, c.Request)
}
