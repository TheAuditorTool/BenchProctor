// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest65920 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest65920.class);

    @GET
    @Path("/BenchmarkTest65920")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest65920(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        LOG.info("Action: {}", headerValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
