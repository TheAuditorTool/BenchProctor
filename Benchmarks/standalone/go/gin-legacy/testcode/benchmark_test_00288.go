// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00288(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data := func(v string) string { return strings.TrimSpace(v) }(cookieValue)
	tokenRNG := rand.New(rand.NewSource(time.Now().UnixNano()))
	apiToken := fmt.Sprintf("%016x", tokenRNG.Uint64())
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
