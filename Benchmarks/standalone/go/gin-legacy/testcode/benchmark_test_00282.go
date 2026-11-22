// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00282(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := uaValue
	if _, after, ok := strings.Cut(uaValue, ","); ok {
		data = after
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
