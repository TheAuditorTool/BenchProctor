// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00020(c *gin.Context) {
	hostValue := c.Request.Host
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(hostValue)
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	c.Redirect(http.StatusFound, targetUrl)
}
