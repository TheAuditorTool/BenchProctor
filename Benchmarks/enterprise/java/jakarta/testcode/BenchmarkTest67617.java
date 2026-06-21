// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest67617 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest67617.class);

    @GET
    @Path("/BenchmarkTest67617")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest67617(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String yamlValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.yaml")))).orElse("");
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(yamlValue, "json");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
