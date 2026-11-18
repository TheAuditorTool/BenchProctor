// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00116(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := dbValue
	if _, after, ok := strings.Cut(dbValue, ","); ok {
		data = after
	}
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
