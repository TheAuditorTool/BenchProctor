// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest15310 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @POST
    @Path("/BenchmarkTest15310")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest15310(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        atomicValue.set(xmlValue);
        String data = atomicValue.get();
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        response.setHeader("Refresh", "0; url=" + processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
