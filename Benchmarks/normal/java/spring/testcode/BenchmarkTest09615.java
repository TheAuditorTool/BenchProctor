// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09615 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @PostMapping("/BenchmarkTest09615")
    public void BenchmarkTest09615(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = collapseWhitespace(fieldValue);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            response.sendRedirect(data);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
