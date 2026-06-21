// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest59645 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GET
    @Path("/BenchmarkTest59645")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest59645(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        FormData payload = new FormData(argValue);
        String data = payload.payload;
        Files.delete(Paths.get("/var/app/data/" + data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
