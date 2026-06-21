// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest21222 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GetMapping("/BenchmarkTest21222")
    public void BenchmarkTest21222(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = toLowerCase(envValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.sendError(500, processed);
    }
}
