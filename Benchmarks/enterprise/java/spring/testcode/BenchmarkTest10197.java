// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10197 {

    @GetMapping("/BenchmarkTest10197")
    public void BenchmarkTest10197(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : refererValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
