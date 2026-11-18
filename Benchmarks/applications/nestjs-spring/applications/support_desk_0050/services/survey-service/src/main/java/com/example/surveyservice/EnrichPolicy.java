// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class EnrichPolicy {


    @GetMapping("/EnrichPolicy")
    public void enrichPolicy(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = origin != null ? origin : "";
        String prefix = remark.length() > 0 ? remark.substring(0, 1).toLowerCase() : "";
        String inquiry;
        switch (prefix) {
            case "h": inquiry = remark.toLowerCase(); break;
            case "f": inquiry = remark.toUpperCase(); break;
            default: inquiry = remark.strip(); break;
        }
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(inquiry)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
