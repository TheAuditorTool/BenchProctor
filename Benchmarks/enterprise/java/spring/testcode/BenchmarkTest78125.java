// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78125 {

    @GetMapping("/BenchmarkTest78125")
    public void BenchmarkTest78125(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        StringBuilder carrier = new StringBuilder();
        carrier.append(envValue);
        String data = carrier.toString();
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException nfe) {
            response.sendError(400, "invalid number"); return;
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
