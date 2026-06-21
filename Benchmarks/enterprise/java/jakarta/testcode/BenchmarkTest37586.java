// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest37586 {

    @GET
    @Path("/BenchmarkTest37586")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest37586(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + secretValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
