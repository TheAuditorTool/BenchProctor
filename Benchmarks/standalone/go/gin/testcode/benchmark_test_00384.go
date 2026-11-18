// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00384(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var data string
	if fieldValue != "" {
		data = fieldValue
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		c.String(http.StatusForbidden, "forbidden host")
		return
	}
	targetUrl := data
	c.Redirect(http.StatusFound, targetUrl)
}
