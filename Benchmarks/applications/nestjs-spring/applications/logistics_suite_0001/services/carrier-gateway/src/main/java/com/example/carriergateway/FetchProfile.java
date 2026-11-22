// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FetchProfile {


    @PostMapping("/FetchProfile")
    public void fetchProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String quotation = field != null ? field : "";
        String prefix = quotation.length() > 0 ? quotation.substring(0, 1).toLowerCase() : "";
        String parcel;
        switch (prefix) {
            case "h": parcel = quotation.toLowerCase(); break;
            case "f": parcel = quotation.toUpperCase(); break;
            default: parcel = quotation.strip(); break;
        }
        Files.write(Paths.get("/var/uploads/" + parcel), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
