// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"encoding/base64"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00077(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	decodedBytes, _ := base64.StdEncoding.DecodeString(dbValue)
	data := string(decodedBytes)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
