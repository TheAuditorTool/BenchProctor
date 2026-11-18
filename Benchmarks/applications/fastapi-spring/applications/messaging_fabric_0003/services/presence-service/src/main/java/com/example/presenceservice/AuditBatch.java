// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class AuditBatch {


    @PostMapping(path="/AuditBatch", consumes="application/xml")
    public void auditBatch(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = xmlBody;
        request.setAttribute("envelope", subject);
        String bulletin = String.valueOf(request.getAttribute("envelope"));
        java.net.URI parsed = java.net.URI.create(bulletin);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String passage = bulletin;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(passage)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
