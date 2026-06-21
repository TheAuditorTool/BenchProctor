// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest21401 {

    @PostMapping(path="/BenchmarkTest21401", consumes="multipart/form-data")
    public void BenchmarkTest21401(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : multipartValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        response.getWriter().print(escaped + ",data");
    }
}
