// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43043 {

    @GetMapping("/BenchmarkTest43043")
    public void BenchmarkTest43043(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = "" + userId;
        if ("https://app.acmecdn.net".equals(data)) response.setHeader("Access-Control-Allow-Origin", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
