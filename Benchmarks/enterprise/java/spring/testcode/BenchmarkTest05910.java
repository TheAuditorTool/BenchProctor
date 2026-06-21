// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05910 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest05910")
    public void BenchmarkTest05910(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = normalize(userId);
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
