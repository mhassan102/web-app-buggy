package app;

public class SeatServlet {
    public void doPost(javax.servlet.http.HttpServletRequest request,
                       javax.servlet.http.HttpServletResponse response) throws java.io.IOException {
        String seat = request.getParameter("seat");
        // BUG: trust_boundary_violation — the request chooses a name that is stored in the session
        request.getSession().setAttribute(seat, "booked");
    }
}
