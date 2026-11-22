// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00224(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := fmt.Sprintf("%s", uaValue)
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
