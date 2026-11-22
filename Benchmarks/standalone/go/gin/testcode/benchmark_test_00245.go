// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00245(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	decodedBytes, _ := base64.StdEncoding.DecodeString(authHeader)
	data := string(decodedBytes)
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
