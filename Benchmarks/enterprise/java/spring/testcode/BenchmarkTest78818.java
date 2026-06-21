// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78818 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @PostMapping("/BenchmarkTest78818")
    public void BenchmarkTest78818(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = expandTabs(fieldValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        if ("admin".equals(processed) || "ROLE_ADMIN".equals(processed)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
