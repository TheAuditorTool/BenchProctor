// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00352(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := strings.Join(strings.FieldsFunc(forwardedIP, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
