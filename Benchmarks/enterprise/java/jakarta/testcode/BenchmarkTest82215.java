// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest82215 {

    @POST
    @Path("/BenchmarkTest82215")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82215(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Properties holder = new java.util.Properties();
        holder.load(new java.io.StringReader("rawValue=" + xmlValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", holder.getProperty("format", "plain"));
        String data = holder.getProperty("rawValue", "");
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
