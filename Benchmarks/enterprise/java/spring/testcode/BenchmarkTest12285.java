// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12285 {

    @GetMapping("/BenchmarkTest12285")
    public void BenchmarkTest12285(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        System.loadLibrary(envValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
