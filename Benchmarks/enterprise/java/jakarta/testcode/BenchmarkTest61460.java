// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest61460 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest61460.class);

    @GET
    @Path("/BenchmarkTest61460")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest61460(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String configValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.json")))).orElse("");
        String data;
        try { data = String.valueOf(Integer.parseInt(configValue)); }
        catch (NumberFormatException e) { data = configValue; }
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
