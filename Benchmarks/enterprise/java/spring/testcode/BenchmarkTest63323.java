// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63323 {

    @GetMapping("/BenchmarkTest63323")
    public void BenchmarkTest63323(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(userId);
        String data = envelope.toString();
        System.setProperty("app.user.preference", data);
        response.setHeader("X-Config-Set", "app.user.preference");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
