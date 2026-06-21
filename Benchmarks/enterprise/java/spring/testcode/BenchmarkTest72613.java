// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest72613 {

    @PostMapping(path="/BenchmarkTest72613", consumes="multipart/form-data")
    public void BenchmarkTest72613(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Function<String, String> primary = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::trim);
        String data = stripChain.apply(uploadName);
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
