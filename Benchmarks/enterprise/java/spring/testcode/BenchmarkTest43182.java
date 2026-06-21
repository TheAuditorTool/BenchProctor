// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43182 {

    @PostMapping("/BenchmarkTest43182")
    public void BenchmarkTest43182(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = String.join(" ", fieldValue.split("\\s+"));
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
