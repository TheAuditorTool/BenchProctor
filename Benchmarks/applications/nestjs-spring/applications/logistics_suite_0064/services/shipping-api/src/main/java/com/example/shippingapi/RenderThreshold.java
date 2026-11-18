// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RenderThreshold {


    @GetMapping("/RenderThreshold")
    public void renderThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> transcript.strip();
        String parcel = valueSupplier.get();
        Files.write(Paths.get("/var/uploads/" + parcel), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
