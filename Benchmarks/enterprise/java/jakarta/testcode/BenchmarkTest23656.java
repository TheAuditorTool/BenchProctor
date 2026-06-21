// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest23656 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest23656")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest23656(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        atomicValue.set(cookieValue);
        String data = atomicValue.get();
        if (!data.matches("^[\\w\\s.\\-:/=\\r\\n]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        response.setHeader("Access-Control-Allow-Origin", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
