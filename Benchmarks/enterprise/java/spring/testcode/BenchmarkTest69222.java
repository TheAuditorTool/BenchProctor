// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69222 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping("/BenchmarkTest69222")
    public void BenchmarkTest69222(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = toLowerCase(commentValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        if ("admin".equals(processed) || "ROLE_ADMIN".equals(processed)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
