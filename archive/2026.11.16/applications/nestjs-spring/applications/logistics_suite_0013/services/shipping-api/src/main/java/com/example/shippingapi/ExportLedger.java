// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportLedger {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/ExportLedger")
    public void exportLedger(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = sessionToken != null ? sessionToken : "";
        String parcel = normalize(footnote);
        String consignment = parcel.matches("^(status|info|list|show)$") ? parcel : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + consignment}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
