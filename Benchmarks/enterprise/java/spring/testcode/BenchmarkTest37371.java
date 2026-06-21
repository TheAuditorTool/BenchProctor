// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37371 {

    @GetMapping("/BenchmarkTest37371/{pathId}")
    public void BenchmarkTest37371(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : pathValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        int result = 100 / Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
