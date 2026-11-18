// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/sqs"
)

func BenchmarkTest00064(w http.ResponseWriter, r *http.Request) {
	var msgValue string
	_sqsOut, _sqsErr := sqsClient.ReceiveMessage(context.Background(), &sqs.ReceiveMessageInput{
		QueueUrl:            aws.String("https://sqs.us-east-1.amazonaws.com/123456789012/app-events"),
		MaxNumberOfMessages: 1,
	})
	if _sqsErr == nil && len(_sqsOut.Messages) > 0 {
		msgValue = aws.ToString(_sqsOut.Messages[0].Body)
	}
	var data string
	for _, token := range strings.Split(msgValue, ",") {
		data = token
	}
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		http.Error(w, "invalid id", http.StatusBadRequest)
		return
	}
	parsedId := strconv.Itoa(_num)
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", parsedId)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
