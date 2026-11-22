// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00229(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	segments := strings.Split(dbValue, ",")
	data := strings.Join(segments, " ")
	const unitPriceCents int32 = 129999
	quantity, err := strconv.ParseInt(data, 10, 32)
	if err != nil {
		c.String(http.StatusBadRequest, "invalid quantity")
		return
	}
	lineTotal := int32(quantity) * unitPriceCents
	DB.Exec("INSERT INTO invoice_lines (sku, qty, total_cents) VALUES ($1, $2, $3)", "SKU-4410", quantity, lineTotal)
	c.JSON(200, gin.H{"code": "OK"})
}
