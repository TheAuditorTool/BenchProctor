// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18477 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @PostMapping(path="/BenchmarkTest18477", consumes="application/xml")
    public void BenchmarkTest18477(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        try { AllowedValue.valueOf(xmlValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { xmlValue = AllowedValue.values()[0].name().toLowerCase(); }
        java.net.URL u = new java.net.URL("https://api.svc.local/lookup?q=" + xmlValue);
        java.net.HttpURLConnection hc = (java.net.HttpURLConnection) u.openConnection();
        hc.connect();
        hc.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
