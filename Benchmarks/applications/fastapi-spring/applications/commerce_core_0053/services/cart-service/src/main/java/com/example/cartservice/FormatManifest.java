// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class FormatManifest {


    @GetMapping("/FormatManifest/{pathId}")
    public void formatManifest(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = pathId;
        String prefix = memo.length() > 0 ? memo.substring(0, 1).toLowerCase() : "";
        String voucher;
        switch (prefix) {
            case "h": voucher = memo.toLowerCase(); break;
            case "f": voucher = memo.toUpperCase(); break;
            default: voucher = memo.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + voucher));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
