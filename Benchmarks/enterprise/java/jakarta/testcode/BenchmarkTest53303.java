// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest53303 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest53303.class);

    @GET
    @Path("/BenchmarkTest53303")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest53303(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), authHeader);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
