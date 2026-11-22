// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00220(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", fieldValue)
	data := relayBuilder.String()
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid id")
		return
	}
	parsedId := strconv.Itoa(_num)
	var matched []User
	if err := gormDB.Raw("SELECT id, name FROM users WHERE id = ?", parsedId).Scan(&matched).Error; err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(200, gin.H{"code": "OK"})
}
