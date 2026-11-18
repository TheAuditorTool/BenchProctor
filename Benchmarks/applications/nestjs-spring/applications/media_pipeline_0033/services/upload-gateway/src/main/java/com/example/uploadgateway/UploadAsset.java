// SPDX-License-Identifier: Apache-2.0
package com.example.uploadgateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;

@RestController
class UploadAsset {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("media_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/UploadAsset")
    public void uploadAsset(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = inboundPayload.value != null ? inboundPayload.value : "";
        java.net.URI parsed = java.net.URI.create(blurb);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.matches("^(api\\.svc\\.local|cdn\\.acmecdn\\.net)$")) { response.sendError(403); return; }
        String montage = blurb;
        String socketRaw = String.valueOf(montage);
        String socketHost = socketRaw.contains("://") ? java.net.URI.create(socketRaw).getHost() : socketRaw;
        new Socket(socketHost, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
