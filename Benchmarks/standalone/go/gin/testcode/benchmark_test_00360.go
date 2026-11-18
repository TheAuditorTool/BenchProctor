// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00360(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	sum := sha256.Sum256([]byte(authHeader))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
