// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12313 {

    @GetMapping("/BenchmarkTest12313")
    public void BenchmarkTest12313(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        StringBuilder envelope = new StringBuilder();
        envelope.append(argValue);
        String data = envelope.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
