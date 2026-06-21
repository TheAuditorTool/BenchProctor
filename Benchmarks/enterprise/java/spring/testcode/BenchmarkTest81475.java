// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81475 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GetMapping("/BenchmarkTest81475")
    public void BenchmarkTest81475(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        try { AllowedValue.valueOf(headerValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { headerValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + headerValue + "\"}");
    }
}
