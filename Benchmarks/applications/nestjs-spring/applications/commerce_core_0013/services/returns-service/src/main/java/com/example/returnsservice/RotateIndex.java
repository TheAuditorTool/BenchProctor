// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
class RotateIndex {


    @GetMapping("/RotateIndex")
    public void rotateIndex(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = host != null ? host : "";
        String backorder = wording.isEmpty() ? "default" : wording;
        String voucher = backorder.matches("^(config|data|index|schema)$") ? backorder : "config";
        Files.write(Paths.get("/var/uploads/" + voucher), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
