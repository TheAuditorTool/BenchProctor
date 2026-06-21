// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest33858 {

    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest33858")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest33858(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        ref.set(originValue);
        String data = ref.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + processed + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
