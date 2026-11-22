// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PruneBundle {


    @GetMapping("/PruneBundle")
    public void pruneBundle(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = userAgent != null ? userAgent : "";
        String backorder;
        try { backorder = String.valueOf(Integer.parseInt(notice)); }
        catch (NumberFormatException e) { backorder = notice; }
        java.nio.file.Path baseName = java.nio.file.Paths.get(backorder).getFileName();
        String voucher = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        String content = Files.readString(Paths.get(voucher), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
