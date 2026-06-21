// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41782 {

    @GetMapping("/BenchmarkTest41782")
    public void BenchmarkTest41782(HttpServletRequest request, HttpServletResponse response) throws Exception {
        response.sendError(403, "directory listing forbidden");
    }
}
