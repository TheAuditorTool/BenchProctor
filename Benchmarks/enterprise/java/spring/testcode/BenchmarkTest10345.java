// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10345 {

    private enum AllowedValue { APPLICATION_JSON, TEXT_PLAIN, TEXT_HTML, APPLICATION_XML }

    @GetMapping("/BenchmarkTest10345")
    public void BenchmarkTest10345(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        try { AllowedValue.valueOf(refererValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { refererValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setHeader("X-Forwarded-For", refererValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
