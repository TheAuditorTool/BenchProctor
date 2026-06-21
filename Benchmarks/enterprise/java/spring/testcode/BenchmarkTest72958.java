// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest72958 {

    @GetMapping("/BenchmarkTest72958")
    public void BenchmarkTest72958(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = "[%s]".formatted(userId);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
