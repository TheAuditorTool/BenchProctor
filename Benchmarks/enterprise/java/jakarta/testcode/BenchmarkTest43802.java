// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43802 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();
    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest43802.class);

    @GET
    @Path("/BenchmarkTest43802")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43802(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        stateBox.set(cookieValue);
        String data = stateBox.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        LOG.info("Action: {}", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
