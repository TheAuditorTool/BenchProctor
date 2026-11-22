// SPDX-License-Identifier: Apache-2.0
package com.example.watchlistsync;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class SyncWatchlist {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("risk_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/SyncWatchlist")
    public void syncWatchlist(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = inboundPayload.value != null ? inboundPayload.value : "";
        Files.delete(Paths.get("/var/app/data/" + note));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
