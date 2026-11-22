// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class MergeProfile {


    @GetMapping("/MergeProfile")
    public void mergeProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = host != null ? host : "";
        String backorder = notice.isEmpty() ? "default" : notice;
        String voucher = backorder.matches("^(config|data|index|schema)$") ? backorder : "config";
        Files.write(Paths.get("/var/uploads/" + voucher), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
