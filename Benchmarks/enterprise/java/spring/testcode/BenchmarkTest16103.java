// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16103 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @PostMapping("/BenchmarkTest16103")
    public void BenchmarkTest16103(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        try { AllowedValue.valueOf(commentValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { commentValue = AllowedValue.values()[0].name().toLowerCase(); }
        java.net.URL u = new java.net.URL("https://api.svc.local/lookup?q=" + commentValue);
        java.net.HttpURLConnection hc = (java.net.HttpURLConnection) u.openConnection();
        hc.connect();
        hc.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
