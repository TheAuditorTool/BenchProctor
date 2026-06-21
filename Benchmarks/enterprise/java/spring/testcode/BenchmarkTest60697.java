// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60697 {

    @PostMapping("/BenchmarkTest60697")
    public void BenchmarkTest60697(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        response.sendError(500, "Internal error");
    }
}
