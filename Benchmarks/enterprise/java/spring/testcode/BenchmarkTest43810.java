// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43810 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest43810")
    public void BenchmarkTest43810(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        response.setHeader("Access-Control-Allow-Origin", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
