// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest45893 {

    @PostMapping(path="/BenchmarkTest45893", consumes="multipart/form-data")
    public void BenchmarkTest45893(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Function<String, String> primary = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::trim);
        String data = stripChain.apply(uploadName);
        if (!data.matches("^[\\w\\s<>\\\"'/().;=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.getWriter().print("<div>" + data + "</div>");
    }
}
