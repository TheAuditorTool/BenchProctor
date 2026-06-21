// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.parsers.*;

@Path("/")
public class BenchmarkTest21851 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest21851")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21851(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
