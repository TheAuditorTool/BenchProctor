<%@ page contentType="text/html;charset=UTF-8" %>
<%
    String hiddenFormField = (String) request.getAttribute("hidden_form_field");
    if ("admin".equals(hiddenFormField)) {
        out.print("<p>admin override accepted: " + hiddenFormField + "</p>");
    } else {
        out.print("<p>standard view</p>");
    }
%>
