// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00257(c *gin.Context) {
	header, err := c.FormFile("upload")
	if err != nil {
		c.String(http.StatusBadRequest, "bad upload")
		return
	}
	uploadName := header.Filename
	relayPrefix := ""
	if len(uploadName) > 0 {
		relayPrefix = strings.ToLower(uploadName[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = uploadName
	case "f":
		data = uploadName
	default:
		data = uploadName
	}
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	c.JSON(http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
