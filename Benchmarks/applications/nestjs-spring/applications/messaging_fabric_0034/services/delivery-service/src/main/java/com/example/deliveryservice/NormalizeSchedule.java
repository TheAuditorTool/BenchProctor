// SPDX-License-Identifier: Apache-2.0
package com.example.deliveryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class NormalizeSchedule {


    @GetMapping("/NormalizeSchedule")
    public void normalizeSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> footnote.strip();
        String bulletin = valueSupplier.get();
        Files.write(Paths.get("/var/uploads/" + bulletin), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
