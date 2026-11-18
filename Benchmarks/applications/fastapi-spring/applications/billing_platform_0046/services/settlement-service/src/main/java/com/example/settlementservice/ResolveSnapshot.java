// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class ResolveSnapshot {


    @GetMapping("/ResolveSnapshot/{pathId}")
    public void resolveSnapshot(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = pathId;
        String prefix = remark.length() > 0 ? remark.substring(0, 1).toLowerCase() : "";
        String remittance;
        switch (prefix) {
            case "h": remittance = remark.toLowerCase(); break;
            case "f": remittance = remark.toUpperCase(); break;
            default: remittance = remark.strip(); break;
        }
        Files.delete(Paths.get("/var/app/data/" + remittance));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
