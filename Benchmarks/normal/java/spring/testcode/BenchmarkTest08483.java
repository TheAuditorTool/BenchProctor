// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08483 {

    @PostMapping("/BenchmarkTest08483")
    public void BenchmarkTest08483(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data;
        if (fieldValue.length() > 256) { data = fieldValue.substring(0, 256); }
        else { data = fieldValue; }
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        response.getWriter().print(escaped + ",data");
    }
}
