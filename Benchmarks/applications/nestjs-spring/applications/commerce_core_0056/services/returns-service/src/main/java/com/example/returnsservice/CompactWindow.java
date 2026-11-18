// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CompactWindow {


    @GetMapping("/CompactWindow")
    public void compactWindow(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> citation.strip();
        String backorder = valueSupplier.get();
        Files.write(Paths.get("/var/uploads/" + backorder), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
