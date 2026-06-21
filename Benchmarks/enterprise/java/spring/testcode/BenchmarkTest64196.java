// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64196 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest64196")
    public void BenchmarkTest64196(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = normalize(userId);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
