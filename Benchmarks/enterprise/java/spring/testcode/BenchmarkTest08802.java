// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08802 {

    @GetMapping("/BenchmarkTest08802")
    public void BenchmarkTest08802(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + envValue;
        String data = valueSupplier.get();
        int divisor = Integer.parseInt(data);
        if (divisor == 0) { response.sendError(400); return; }
        int result = 100 / divisor;
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
