// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00148(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := strings.Join(strings.FieldsFunc(dbValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	orderDoc, parseErr := xmlquery.Parse(strings.NewReader(data))
	if parseErr != nil {
		c.String(http.StatusBadRequest, "malformed order")
		return
	}
	totalNode := xmlquery.FindOne(orderDoc, "//order/total")
	orderTotal := totalNode.InnerText()
	c.JSON(http.StatusOK, map[string]string{"total": orderTotal})
}
