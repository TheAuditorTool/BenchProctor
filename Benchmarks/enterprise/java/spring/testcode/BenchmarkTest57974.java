// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57974 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest57974")
    public void BenchmarkTest57974(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = normalize(envValue);
        response.sendError(500, data);
    }
}
