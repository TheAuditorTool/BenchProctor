// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36910 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest36910")
    public void BenchmarkTest36910(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        request.getSession().setMaxInactiveInterval(900);
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
