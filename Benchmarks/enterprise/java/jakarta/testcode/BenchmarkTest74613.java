// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest74613 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest74613.class);

    @GET
    @Path("/BenchmarkTest74613")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest74613(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String yamlValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.yaml")))).orElse("");
        String data = yamlValue.isEmpty() ? "default" : yamlValue;
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
