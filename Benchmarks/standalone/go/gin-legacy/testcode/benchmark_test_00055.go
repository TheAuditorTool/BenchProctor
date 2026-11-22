// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00055(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var data string
	for _, token := range strings.Split(refererValue, ",") {
		data = token
	}
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		c.String(http.StatusBadRequest, "malformed order")
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	orderTotal := totalNode.InnerText()
	c.JSON(http.StatusOK, map[string]string{"total": orderTotal})
}
