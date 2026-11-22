// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00125(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	var parsed map[string]interface{}
	json.Unmarshal([]byte(jsonValue), &parsed)
	data, _ := parsed["value"].(string)
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
	body, _ := ioutil.ReadAll(resp.Body)
	c.Data(200, "text/plain", body)
}
