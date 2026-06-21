// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03697 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest03697.class);

    @GET
    @Path("/BenchmarkTest03697")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03697(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.function.Function<String, String> firstStage = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::trim);
        String data = composed.apply(authHeader);
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
