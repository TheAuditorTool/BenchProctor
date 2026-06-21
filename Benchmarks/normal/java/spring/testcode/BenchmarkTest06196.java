// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06196 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest06196")
    public void BenchmarkTest06196(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = trimEnds(userId);
        System.setProperty("app.user.preference", data);
        response.setHeader("X-Config-Set", "app.user.preference");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
