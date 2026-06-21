// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75065 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest75065")
    public void BenchmarkTest75065(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        response.getWriter().print(data + ",data\n");
    }
}
