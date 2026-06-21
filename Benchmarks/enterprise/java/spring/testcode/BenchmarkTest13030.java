// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13030 {

    @PostMapping("/BenchmarkTest13030")
    public void BenchmarkTest13030(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        request.getSession().setAttribute("data", String.valueOf(fieldValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
