// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.xpath.*;

@Path("/")
public class BenchmarkTest09259 {

    private enum AllowedValue { ADMIN, OPERATOR, VIEWER, AUDITOR }

    @GET
    @Path("/BenchmarkTest09259")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09259(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = "" + authHeader;
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        xpath.evaluate("/users/user[@name='" + data + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
