// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class BenchmarkTest16692 {

    @GET
    @Path("/BenchmarkTest16692/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16692(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        StringBuilder bundle = new StringBuilder();
        bundle.append(pathValue);
        String data = bundle.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Yaml yaml = new Yaml();
            Object obj = yaml.load(data);
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
