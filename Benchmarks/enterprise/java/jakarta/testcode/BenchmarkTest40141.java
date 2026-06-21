// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest40141 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest40141.class);

    @GET
    @Path("/BenchmarkTest40141")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest40141(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : propValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
