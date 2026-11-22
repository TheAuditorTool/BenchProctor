// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00276(c *gin.Context) {
	pathValue := c.Param("id")
	var data string
	if len(pathValue) > 0 {
		data = pathValue
	} else {
		data = "default"
	}
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid integer")
		return
	}
	boundedVal := strconv.Itoa(max(0, min(_num, 2147483647)))
	const unitPriceCents int32 = 129999
	quantity, err := strconv.ParseInt(boundedVal, 10, 32)
	if err != nil {
		c.String(http.StatusBadRequest, "invalid quantity")
		return
	}
	lineTotal := int64(quantity) * int64(unitPriceCents)
	DB.Exec("INSERT INTO invoice_lines (sku, qty, total_cents) VALUES ($1, $2, $3)", "SKU-4410", quantity, lineTotal)
	c.JSON(200, gin.H{"code": "OK"})
}
