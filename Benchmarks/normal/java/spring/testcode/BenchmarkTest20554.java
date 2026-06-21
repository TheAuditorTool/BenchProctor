// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20554 {

    @GetMapping("/BenchmarkTest20554")
    public void BenchmarkTest20554(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        response.sendRedirect(userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
