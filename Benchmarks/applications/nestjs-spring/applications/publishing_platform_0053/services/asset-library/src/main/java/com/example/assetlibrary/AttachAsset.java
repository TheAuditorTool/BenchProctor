// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.net.*;
import java.io.*;

@RestController
class AttachAsset {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("publishing_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/AttachAsset")
    public void attachAsset(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = inboundPayload.value != null ? inboundPayload.value : "";
        java.net.URI parsed = java.net.URI.create(remark);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String addendum = remark;
        try {
            java.net.http.HttpRequest httpReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(addendum)).GET().build();
            java.net.http.HttpResponse<String> httpResp = java.net.http.HttpClient.newHttpClient().send(httpReq, java.net.http.HttpResponse.BodyHandlers.ofString());
            response.setHeader("X-Fetch-Status", String.valueOf(httpResp.statusCode()));
        } catch (Exception e) { response.sendError(502); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
