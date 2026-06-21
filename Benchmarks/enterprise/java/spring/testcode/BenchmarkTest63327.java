// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63327 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GetMapping("/BenchmarkTest63327")
    public void BenchmarkTest63327(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + headerValue;
        String data = valueSupplier.get();
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        java.net.URL u = new java.net.URL("https://api.svc.local/lookup?q=" + data);
        java.net.HttpURLConnection hc = (java.net.HttpURLConnection) u.openConnection();
        hc.connect();
        hc.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
