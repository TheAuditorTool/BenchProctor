// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69204 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest69204")
    public void BenchmarkTest69204(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        response.getWriter().print(String.valueOf(data));
    }
}
