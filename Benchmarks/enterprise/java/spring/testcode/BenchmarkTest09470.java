// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09470 {

    @GetMapping("/BenchmarkTest09470")
    public void BenchmarkTest09470(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + cookieValue;
        String data = valueSupplier.get();
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
