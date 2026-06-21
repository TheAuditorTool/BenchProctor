// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest48054 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest48054.class);

    @GET
    @Path("/BenchmarkTest48054")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest48054(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        LOG.info("Action: {}", dotenvValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
