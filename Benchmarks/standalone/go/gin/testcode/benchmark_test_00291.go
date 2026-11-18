// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00291(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	hexBytes, _ := hex.DecodeString(dbValue)
	data := string(hexBytes)
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	c.JSON(http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
