// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00258(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	var data string
	if cookieValue != "" {
		data = cookieValue
	}
	upstreamReq, err := http.NewRequest(http.MethodGet, data, nil)
	if err != nil {
		c.String(http.StatusBadRequest, err.Error())
		return
	}
	upstreamReq.Header.Set("Accept", "application/json")
	resp, err := http.DefaultClient.Do(upstreamReq)
	if err != nil {
		c.String(http.StatusBadGateway, err.Error())
		return
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	c.Data(200, "text/plain", body)
}
