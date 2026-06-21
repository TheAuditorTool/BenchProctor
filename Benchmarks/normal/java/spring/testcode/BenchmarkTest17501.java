// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17501 {

    @PostMapping("/BenchmarkTest17501")
    public void BenchmarkTest17501(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", fieldValue);
        String data = sw.toString();
        int result = 100 / Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
