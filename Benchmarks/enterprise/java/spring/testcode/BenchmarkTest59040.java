// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59040 {

    @GetMapping("/BenchmarkTest59040")
    public void BenchmarkTest59040(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        new java.io.File(userId).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
