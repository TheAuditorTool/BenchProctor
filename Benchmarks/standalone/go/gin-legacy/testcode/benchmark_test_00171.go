// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00171(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := func(v string) string { return strings.TrimSpace(v) }(redisValue)
	resp, err := http.Get(data)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)
	c.Data(200, "text/plain", body)
}
