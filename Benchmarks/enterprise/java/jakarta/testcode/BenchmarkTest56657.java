// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest56657 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest56657.class);

    @GET
    @Path("/BenchmarkTest56657")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest56657(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = java.util.Arrays.asList(headerValue.split(","));
        String data = String.join(",", tokens);
        LOG.info("request processed");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
