// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest46869 {

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest46869")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest46869(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        sharedRef.set(authHeader);
        String data = sharedRef.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        byte[] buf = new byte[Integer.parseInt(processed)];
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
