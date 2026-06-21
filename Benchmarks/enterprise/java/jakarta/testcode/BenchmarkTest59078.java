// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest59078 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest59078/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest59078(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        stateBox.set(pathValue);
        String data = stateBox.get();
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + processed + "\">", MediaType.TEXT_HTML).build();
    }
}
