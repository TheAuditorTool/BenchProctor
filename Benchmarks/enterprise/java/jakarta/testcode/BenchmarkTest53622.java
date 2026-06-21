// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest53622 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest53622.class);

    @GET
    @Path("/BenchmarkTest53622")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest53622(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String yamlValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.yaml")))).orElse("");
        LOG.info("Action: {}", yamlValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
