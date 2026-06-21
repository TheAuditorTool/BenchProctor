// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34202 {

    @PostMapping("/BenchmarkTest34202")
    public void BenchmarkTest34202(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(fieldValue);
        String data = bundle.toString();
        response.sendError(500, data);
    }
}
