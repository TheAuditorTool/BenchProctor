// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72425 {

    @GetMapping("/BenchmarkTest72425")
    public void BenchmarkTest72425(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + cookieValue;
        String data = valueSupplier.get();
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
