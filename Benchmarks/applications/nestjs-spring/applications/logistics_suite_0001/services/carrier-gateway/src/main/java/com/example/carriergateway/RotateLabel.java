// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RotateLabel {


    @GetMapping("/RotateLabel")
    public void rotateLabel(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = userAgent != null ? userAgent : "";
        String parcel;
        try { parcel = String.valueOf(Integer.parseInt(quotation)); }
        catch (NumberFormatException e) { parcel = quotation; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(parcel).getFileName();
        String consignment = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(consignment), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
