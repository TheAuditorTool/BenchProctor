// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03349 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest03349.class);

    @GET
    @Path("/BenchmarkTest03349")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03349(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(dotenvValue, "cookie");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
