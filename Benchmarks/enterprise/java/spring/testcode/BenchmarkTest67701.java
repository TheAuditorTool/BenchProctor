// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67701 {

    @PostMapping("/BenchmarkTest67701")
    public void BenchmarkTest67701(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = String.format("%s", fieldValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
