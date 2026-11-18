// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportIndex {


    @GetMapping("/ExportIndex")
    public void exportIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = authorization != null ? authorization : "";
        String parcel;
        try { parcel = new String(java.util.Base64.getDecoder().decode(transcript), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { parcel = transcript; }
        String consignment = parcel.matches("^(status|info|list|show)$") ? parcel : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + consignment}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
