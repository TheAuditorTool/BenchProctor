// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03669 {

    @GetMapping("/BenchmarkTest03669")
    public void BenchmarkTest03669(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if ("https://app.acmecdn.net".equals(userId)) response.setHeader("Access-Control-Allow-Origin", userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
