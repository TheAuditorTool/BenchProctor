// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13984 {

    @GetMapping("/BenchmarkTest13984")
    public void BenchmarkTest13984(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (!new java.io.File("/var/app/data", new java.io.File(userId).getName()).delete()) { response.sendError(500, "delete failed"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
