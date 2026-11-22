// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PullSupplierFeed {

    private static class InboundPayload {
        @com.fasterxml.jackson.annotation.JsonProperty("inventory_payload")
        public String value;
        public InboundPayload() {}
    }

    @PostMapping("/PullSupplierFeed")
    public void pullSupplierFeed(@RequestBody InboundPayload inboundPayload, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = inboundPayload.value != null ? inboundPayload.value : "";
        response.getWriter().print("<div>" + memo + "</div>");
    }
}
