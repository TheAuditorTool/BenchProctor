// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01770 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest01770")
    public void BenchmarkTest01770(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        System.setProperty("app.user.preference", data);
        response.setHeader("X-Config-Set", "app.user.preference");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
