// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12377 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GET
    @Path("/BenchmarkTest12377")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12377(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = stripCRLF(hostValue);
        if ("https://app.acmecdn.net".equals(data)) response.setHeader("Access-Control-Allow-Origin", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
