// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71314 {

    @PostMapping("/BenchmarkTest71314")
    public void BenchmarkTest71314(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        response.getWriter().print("<div>" + fieldValue + "</div>");
    }
}
