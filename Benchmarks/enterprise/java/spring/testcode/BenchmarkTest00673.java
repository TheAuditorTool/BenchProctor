// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00673 {

    private static String normalize(String v) { return v.strip(); }
    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @PostMapping(path="/BenchmarkTest00673", consumes="text/plain")
    public void BenchmarkTest00673(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = normalize(rawData);
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
