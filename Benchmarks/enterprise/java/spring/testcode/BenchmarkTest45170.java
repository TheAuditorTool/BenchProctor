// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest45170 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest45170")
    public void BenchmarkTest45170(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        stateBox.set(envValue);
        String data = stateBox.get();
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
