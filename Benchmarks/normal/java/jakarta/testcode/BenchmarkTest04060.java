// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04060 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest04060.class);
    private enum AllowedValue { INFO, WARN, ERROR, DEBUG }

    @GET
    @Path("/BenchmarkTest04060")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04060(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        try { AllowedValue.valueOf(headerValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { headerValue = AllowedValue.values()[0].name().toLowerCase(); }
        LOG.info("Action: {}", headerValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
