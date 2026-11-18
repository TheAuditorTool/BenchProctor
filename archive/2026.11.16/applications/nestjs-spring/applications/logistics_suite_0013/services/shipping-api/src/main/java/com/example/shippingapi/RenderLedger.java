// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderLedger {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/RenderLedger")
    public void renderLedger(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(System.getenv("SHIPPING_INPUT_0013")).orElse("");
        String parcel = normalize(footnote);
        Files.delete(Paths.get("/var/app/data/" + parcel));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
