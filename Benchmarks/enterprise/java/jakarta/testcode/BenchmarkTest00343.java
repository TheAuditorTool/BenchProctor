// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.parsers.*;

@Path("/")
public class BenchmarkTest00343 {

    @GET
    @Path("/BenchmarkTest00343")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00343(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(authHeader)));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
