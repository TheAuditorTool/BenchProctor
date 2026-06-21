// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05011 {

    @PostMapping("/BenchmarkTest05011")
    public void BenchmarkTest05011(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        response.sendRedirect(fieldValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
