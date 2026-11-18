// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00012(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	capture := func() string { return strings.TrimSpace(headerValue) }
	data := capture()
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
