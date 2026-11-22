// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00212(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var data string
	if len(refererValue) > 0 {
		data = refererValue
	} else {
		data = "default"
	}
	tokenBytes := make([]byte, 16)
	_, err := io.ReadFull(rand.Reader, tokenBytes)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	apiToken := hex.EncodeToString(tokenBytes)
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
