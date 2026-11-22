// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00030(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(graphqlVar)
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		c.String(http.StatusBadRequest, "malformed order")
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	if totalNode == nil {
		c.String(http.StatusBadRequest, "order total missing")
		return
	}
	orderTotal := totalNode.InnerText()
	c.JSON(http.StatusOK, map[string]string{"total": orderTotal})
}
