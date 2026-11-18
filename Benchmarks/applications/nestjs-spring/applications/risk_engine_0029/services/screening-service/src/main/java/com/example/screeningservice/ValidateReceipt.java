// SPDX-License-Identifier: Apache-2.0
package com.example.screeningservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class ValidateReceipt {


    @GetMapping("/ValidateReceipt")
    public void validateReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = origin != null ? origin : "";
        String prefix = subject.length() > 0 ? subject.substring(0, 1).toLowerCase() : "";
        String grievance;
        switch (prefix) {
            case "h": grievance = subject.toLowerCase(); break;
            case "f": grievance = subject.toUpperCase(); break;
            default: grievance = subject.strip(); break;
        }
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(grievance)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
