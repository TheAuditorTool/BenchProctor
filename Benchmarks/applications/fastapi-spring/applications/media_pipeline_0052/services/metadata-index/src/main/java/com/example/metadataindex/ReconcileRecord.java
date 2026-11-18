// SPDX-License-Identifier: Apache-2.0
package com.example.metadataindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class ReconcileRecord {


    @PostMapping(path="/ReconcileRecord", consumes="text/plain")
    public void reconcileRecord(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String tagline = rawBody != null ? rawBody : "";
        String rendition = String.join(" ", tagline.split("[ \\t]+"));
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(rendition)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
