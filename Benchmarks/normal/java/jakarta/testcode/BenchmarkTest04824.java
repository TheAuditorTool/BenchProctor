// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest04824 {

    @GET
    @Path("/BenchmarkTest04824")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04824(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = String.format("payload=%s", originValue);
        URL url = java.net.URI.create("http://" + data).toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        try {
            conn.connect();
            conn.getInputStream().close();
        } finally { conn.disconnect(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
