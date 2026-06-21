// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75763 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest75763")
    public void BenchmarkTest75763(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        valueRef.set(cookieValue);
        String data = valueRef.get();
        if (System.currentTimeMillis() > 1000000000000L) {
            new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
