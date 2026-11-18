// SPDX-License-Identifier: Apache-2.0
package com.example.bouncehandler;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class CompactLedger {


    @GetMapping("/CompactLedger/{pathId}")
    public void compactLedger(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = pathId;
        String bulletin;
        try { bulletin = String.valueOf(Integer.parseInt(summary)); }
        catch (NumberFormatException e) { bulletin = summary; }
        Files.delete(Paths.get("/var/app/data/" + bulletin));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
