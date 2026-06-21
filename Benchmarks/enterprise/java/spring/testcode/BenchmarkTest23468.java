// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23468 {

    @PostMapping(path="/BenchmarkTest23468", consumes="text/plain")
    public void BenchmarkTest23468(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        response.sendError(403, "directory listing forbidden");
    }
}
