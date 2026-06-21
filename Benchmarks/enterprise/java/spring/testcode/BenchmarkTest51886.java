// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51886 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GetMapping("/BenchmarkTest51886")
    public void BenchmarkTest51886(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        try { AllowedValue.valueOf(headerValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { headerValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setContentType("text/html");
        response.getWriter().print(headerValue);
    }
}
