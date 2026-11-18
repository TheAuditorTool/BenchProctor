// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class NormalizeFulfillment {


    @GetMapping("/NormalizeFulfillment")
    public void normalizeFulfillment(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> heading.strip();
        String voucher = valueSupplier.get();
        Files.write(Paths.get("/var/uploads/" + voucher), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
