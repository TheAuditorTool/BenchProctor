// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha1"
	"encoding/hex"
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00143(c *gin.Context) {
	userID := c.Query("id")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(userID)
	digest := sha1.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
