// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest40619 {

    @PostMapping("/BenchmarkTest40619")
    public void BenchmarkTest40619(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = fieldValue.replace("\u0000", "");
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        response.getWriter().print(escaped + ",data");
    }
}
