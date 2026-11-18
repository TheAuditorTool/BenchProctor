// SPDX-License-Identifier: Apache-2.0
package com.example.paymentgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class CapturePayment {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("billing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/CapturePayment")
    public void capturePayment(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String arrears = inboundPayload.value != null ? inboundPayload.value : "";
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(arrears)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
