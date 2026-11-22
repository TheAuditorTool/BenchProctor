// SPDX-License-Identifier: Apache-2.0
package com.example.watchlistsync;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

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
        class SchemaInput {
            @javax.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%\\-]+$") final String value;
            SchemaInput(String value) { this.value = value; }
        }
        javax.validation.Validator schemaValidator = javax.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(note)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + note});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
