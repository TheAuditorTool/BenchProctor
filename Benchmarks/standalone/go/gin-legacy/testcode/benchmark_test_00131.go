// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00131(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	const unitPriceCents int32 = 129999
	quantity, err := strconv.ParseInt(cookieValue, 10, 32)
	if err != nil {
		c.String(http.StatusBadRequest, "invalid quantity")
		return
	}
	lineTotal := int32(quantity) * unitPriceCents
	DB.Exec("INSERT INTO invoice_lines (sku, qty, total_cents) VALUES ($1, $2, $3)", "SKU-4410", quantity, lineTotal)
	c.JSON(200, gin.H{"code": "OK"})
}
