// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00088(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var data string
	if len(authHeader) > 0 {
		data = authHeader
	} else {
		data = "default"
	}
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
