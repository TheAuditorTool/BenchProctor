// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest23750 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest23750.class);

    @GET
    @Path("/BenchmarkTest23750")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest23750(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(envValue);
        String data = normalizer.apply(envValue);
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
