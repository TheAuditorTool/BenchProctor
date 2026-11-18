// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FormatManifest {


    @GetMapping("/FormatManifest")
    public void formatManifest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = xForwardedFor != null ? xForwardedFor : "";
        String voucher;
        try { voucher = String.valueOf(Integer.parseInt(memo)); }
        catch (NumberFormatException e) { voucher = memo; }
        Files.delete(Paths.get("/var/app/data/" + voucher));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
