// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00179(c *gin.Context) {
	fieldValue := c.PostForm("field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(fieldValue)
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
