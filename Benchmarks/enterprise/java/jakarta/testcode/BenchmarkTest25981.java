// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25981 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest25981.class);

    @GET
    @Path("/BenchmarkTest25981")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25981(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        String data = dotenvValue.isEmpty() ? "default" : dotenvValue;
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
