// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest65272 {

    @PostMapping(path="/BenchmarkTest65272", consumes="multipart/form-data")
    public void BenchmarkTest65272(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(uploadName);
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
