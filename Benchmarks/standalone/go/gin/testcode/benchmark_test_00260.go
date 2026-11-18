// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00260(c *gin.Context) {
	hostValue := c.Request.Host
	var data string
	if hostValue != "" {
		data = hostValue
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	c.Redirect(http.StatusFound, targetUrl)
}
