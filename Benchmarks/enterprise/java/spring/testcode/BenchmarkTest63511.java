// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63511 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping("/BenchmarkTest63511")
    public void BenchmarkTest63511(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        valueRef.set(jsonValue);
        String data = valueRef.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        new ProcessBuilder("python3", "-c", processed).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
