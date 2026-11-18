// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00256(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	capture := func() string { return strings.TrimSpace(refererValue) }
	data := capture()
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid id")
		return
	}
	parsedId := strconv.Itoa(_num)
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", parsedId)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
