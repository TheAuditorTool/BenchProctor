// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class BenchmarkTest56327 {

    @GET
    @Path("/BenchmarkTest56327")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest56327(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(headerValue);
        String data = bundle.toString();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            Yaml yaml = new Yaml();
            Object obj = yaml.load(data);
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
