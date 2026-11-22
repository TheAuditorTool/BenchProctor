// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"net/url"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00058(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	capture := func() string { return strings.TrimSpace(graphqlVar) }
	data := capture()
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
