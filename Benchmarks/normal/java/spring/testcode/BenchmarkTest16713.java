// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16713 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping("/BenchmarkTest16713")
    public void BenchmarkTest16713(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        sharedRef.set(jsonValue);
        String data = sharedRef.get();
        if (!data.matches("^[\\w\\s.\\-:/=\\r\\n]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.setHeader("X-Forwarded-For", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
