// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00196(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data := strings.Join(strings.FieldsFunc(cookieValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid integer")
		return
	}
	if _num < 0 {
		_num = 0
	} else if _num > 2147483647 {
		_num = 2147483647
	}
	boundedVal := strconv.Itoa(_num)
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
