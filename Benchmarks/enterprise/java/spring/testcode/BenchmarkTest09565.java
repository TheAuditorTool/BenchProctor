// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09565 {

    private enum AllowedValue { APPLICATION_JSON, TEXT_PLAIN, TEXT_HTML, APPLICATION_XML }

    @GetMapping("/BenchmarkTest09565")
    public void BenchmarkTest09565(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        try { AllowedValue.valueOf(uaValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { uaValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setHeader("X-Forwarded-For", uaValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
