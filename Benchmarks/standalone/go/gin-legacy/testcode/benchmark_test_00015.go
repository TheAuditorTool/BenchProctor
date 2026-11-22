// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00015(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	relayPrefix := ""
	if len(multipartValue) > 0 {
		relayPrefix = strings.ToLower(multipartValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = multipartValue
	case "f":
		data = multipartValue
	default:
		data = multipartValue
	}
	upstreams := map[string]*url.URL{
		"billing": {Scheme: "https", Host: "billing.svc.cluster"},
		"reports": {Scheme: "https", Host: "reports.svc.cluster"},
	}
	upstream := upstreams[data]
	if upstream == nil {
		c.String(http.StatusNotFound, "unknown service")
		return
	}
	upstreamHost := upstream.Host
	c.JSON(http.StatusOK, map[string]string{"upstream": upstreamHost})
}
