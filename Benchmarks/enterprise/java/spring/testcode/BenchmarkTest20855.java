// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20855 {

    @GetMapping("/BenchmarkTest20855")
    public void BenchmarkTest20855(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        byte[] buf = new byte[Integer.parseInt(envValue)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
