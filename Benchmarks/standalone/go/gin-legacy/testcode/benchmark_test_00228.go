// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/md4"
)

func BenchmarkTest00228(c *gin.Context) {
	fieldValue := c.PostForm("field")
	relayPrefix := ""
	if len(fieldValue) > 0 {
		relayPrefix = strings.ToLower(fieldValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = fieldValue
	case "f":
		data = fieldValue
	default:
		data = fieldValue
	}
	legacyDigest := md4.New()
	legacyDigest.Write([]byte(data))
	hashStr := hex.EncodeToString(legacyDigest.Sum(nil))
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
