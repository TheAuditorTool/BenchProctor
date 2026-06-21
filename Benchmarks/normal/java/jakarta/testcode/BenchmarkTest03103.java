// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03103 {

    @GET
    @Path("/BenchmarkTest03103")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03103(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Properties box = new java.util.Properties();
        box.load(new java.io.StringReader("rawValue=" + originValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", box.getProperty("format", "plain"));
        String data = box.getProperty("rawValue", "");
        int[] arr = new int[]{10, 20, 30, 40, 50};
        int idx = Integer.parseInt(data);
        response.setHeader("X-Lookup", String.valueOf(arr[idx]));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
