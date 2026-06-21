// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23487 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @PostMapping("/BenchmarkTest23487")
    public void BenchmarkTest23487(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = collapseWhitespace(fieldValue);
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        response.setHeader("X-Forwarded-For", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
