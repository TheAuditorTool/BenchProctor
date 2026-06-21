// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47347 {

    @GetMapping("/BenchmarkTest47347")
    public void BenchmarkTest47347(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String prefix = envValue.length() > 0 ? envValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = envValue.toLowerCase(); break;
            case "f": data = envValue.toUpperCase(); break;
            default: data = envValue.strip(); break;
        }
        request.getSession().setMaxInactiveInterval(900);
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
