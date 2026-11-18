// SPDX-License-Identifier: Apache-2.0
package com.example.mfaservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class ArchiveCheckpoint {


    @PostMapping(path="/ArchiveCheckpoint", consumes="application/xml")
    public void archiveCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = xmlBody;
        request.setAttribute("wrapper", snippet);
        String persona = String.valueOf(request.getAttribute("wrapper"));
        java.net.URI parsed = java.net.URI.create(persona);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String synopsis = persona;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(synopsis)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
