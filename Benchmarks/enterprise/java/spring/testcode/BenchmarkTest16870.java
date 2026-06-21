// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16870 {

    @PostMapping("/BenchmarkTest16870")
    public void BenchmarkTest16870(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = "" + fieldValue;
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        response.setHeader("X-Forwarded-For", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
