// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67815 {

    @PostMapping("/BenchmarkTest67815")
    public void BenchmarkTest67815(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = "[%s]".formatted(fieldValue);
        response.sendError(500, data);
    }
}
