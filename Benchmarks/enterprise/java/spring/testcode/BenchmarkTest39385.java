// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39385 {

    @PostMapping("/BenchmarkTest39385")
    public void BenchmarkTest39385(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        response.sendError(403, "directory listing forbidden");
    }
}
