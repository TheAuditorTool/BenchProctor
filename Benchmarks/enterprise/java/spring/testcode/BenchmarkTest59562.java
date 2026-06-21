// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59562 {

    @GetMapping("/BenchmarkTest59562")
    public void BenchmarkTest59562(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : apiBody.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
