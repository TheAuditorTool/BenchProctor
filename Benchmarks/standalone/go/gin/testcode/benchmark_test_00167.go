// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"io"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00167(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(rawBody)
	tokenLen, _ := strconv.Atoi(data)
	if tokenLen < 16 || tokenLen > 64 {
		tokenLen = 32
	}
	buf := make([]byte, tokenLen)
	rand.Read(buf)
	c.JSON(http.StatusOK, map[string]string{"token": hex.EncodeToString(buf)})
}
