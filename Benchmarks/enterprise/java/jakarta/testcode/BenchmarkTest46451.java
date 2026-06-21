// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest46451 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest46451.class);

    @GET
    @Path("/BenchmarkTest46451")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest46451(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::strip);
        String data = fullPipeline.apply(propValue);
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
