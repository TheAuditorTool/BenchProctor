// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest66178 {

    @PostMapping(path="/BenchmarkTest66178", consumes="multipart/form-data")
    public void BenchmarkTest66178(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = String.join(" ", uploadName.split("\\s+"));
        if (!data.endsWith(".jpg") && !data.endsWith(".png")) { response.sendError(400); return; }
        String entryFile = data;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
