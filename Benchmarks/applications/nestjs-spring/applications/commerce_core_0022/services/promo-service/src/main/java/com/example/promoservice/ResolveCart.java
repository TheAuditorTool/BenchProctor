// SPDX-License-Identifier: Apache-2.0
package com.example.promoservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ResolveCart {


    @GetMapping("/ResolveCart")
    public void resolveCart(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = userAgent != null ? userAgent : "";
        String voucher = subject.isEmpty() ? "default" : subject;
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.%\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(voucher)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + voucher});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
