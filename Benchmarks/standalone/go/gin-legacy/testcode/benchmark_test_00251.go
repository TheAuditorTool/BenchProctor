// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00251(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var data string
	if len(refererValue) > 0 {
		data = refererValue
	} else {
		data = "default"
	}
	upstreams := map[string]*url.URL{
		"billing": {Scheme: "https", Host: "billing.svc.cluster"},
		"reports": {Scheme: "https", Host: "reports.svc.cluster"},
	}
	upstream := upstreams[data]
	upstreamHost := upstream.Host
	c.JSON(http.StatusOK, map[string]string{"upstream": upstreamHost})
}
