// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59954 {

    @GetMapping("/BenchmarkTest59954")
    public void BenchmarkTest59954(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(envValue);
        String data = wrapper.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            System.loadLibrary(data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
