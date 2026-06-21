// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest18688 {

    @GET
    @Path("/BenchmarkTest18688")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18688(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String configValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.json")))).orElse("");
        String prefix = configValue.length() > 0 ? configValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = configValue.toLowerCase(); break;
            case "f": data = configValue.toUpperCase(); break;
            default: data = configValue.strip(); break;
        }
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(data);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
