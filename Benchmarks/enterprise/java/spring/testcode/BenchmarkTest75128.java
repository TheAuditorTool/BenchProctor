// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75128 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GetMapping("/BenchmarkTest75128")
    public void BenchmarkTest75128(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        try { AllowedValue.valueOf(cookieValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { cookieValue = AllowedValue.values()[0].name().toLowerCase(); }
        System.setProperty("app.user.preference", cookieValue);
        response.setHeader("X-Config-Set", "app.user.preference");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
