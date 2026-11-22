// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class PublishPromotion {


    @GetMapping("/PublishPromotion")
    public void publishPromotion(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = authorization != null ? authorization : "";
        String prefix = notice.length() > 0 ? notice.substring(0, 1).toLowerCase() : "";
        String backorder;
        switch (prefix) {
            case "h": backorder = notice.toLowerCase(); break;
            case "f": backorder = notice.toUpperCase(); break;
            default: backorder = notice.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + backorder));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
