// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78446 {

    @GetMapping("/BenchmarkTest78446")
    public void BenchmarkTest78446(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        response.sendError(500, "Internal error");
    }
}
