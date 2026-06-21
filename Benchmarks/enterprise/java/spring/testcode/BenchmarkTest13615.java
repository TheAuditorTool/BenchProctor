// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13615 {

    @PostMapping("/BenchmarkTest13615")
    public void BenchmarkTest13615(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        if (!fieldValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        String normalized = java.text.Normalizer.normalize(fieldValue, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        response.getWriter().print("<p>" + normalized + "</p>");
    }
}
