// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10699 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest10699.class);

    @GET
    @Path("/BenchmarkTest10699")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10699(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        LOG.info("Action: {}", authHeader);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
