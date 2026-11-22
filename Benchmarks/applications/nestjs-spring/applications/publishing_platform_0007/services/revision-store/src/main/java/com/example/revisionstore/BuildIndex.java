// SPDX-License-Identifier: Apache-2.0
package com.example.revisionstore;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class BuildIndex {


    @GetMapping("/BuildIndex")
    public void buildIndex(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = userAgent != null ? userAgent : "";
        java.util.function.Supplier<String> valueSupplier = () -> remark.strip();
        String byline = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + byline}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
