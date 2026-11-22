// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00186(c *gin.Context) {
	pathValue := c.Param("id")
	data := strings.Join(strings.FieldsFunc(pathValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	upstreams := map[string]*url.URL{
		"billing": {Scheme: "https", Host: "billing.svc.cluster"},
		"reports": {Scheme: "https", Host: "reports.svc.cluster"},
	}
	upstream := upstreams[data]
	upstreamHost := upstream.Host
	c.JSON(http.StatusOK, map[string]string{"upstream": upstreamHost})
}
