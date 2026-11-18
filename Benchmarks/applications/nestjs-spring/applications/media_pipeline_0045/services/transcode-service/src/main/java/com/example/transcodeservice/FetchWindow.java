// SPDX-License-Identifier: Apache-2.0
package com.example.transcodeservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class FetchWindow {


    @GetMapping("/FetchWindow")
    public void fetchWindow(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = id != null ? id : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : notice.split(",")) { tokens.add(token.trim()); }
        String rendition = String.join(",", tokens);
        java.net.URI parsed = java.net.URI.create(rendition);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String montage = rendition;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(montage)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
