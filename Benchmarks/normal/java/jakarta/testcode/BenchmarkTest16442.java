// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16442 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();
    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @GET
    @Path("/BenchmarkTest16442")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16442(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        stateBox.set(originValue);
        String data = stateBox.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        sharedLastValue = processed;
        int seen = sharedWriteCount;
        sharedWriteCount = seen + 1;
        return Response.ok().build();
    }
}
