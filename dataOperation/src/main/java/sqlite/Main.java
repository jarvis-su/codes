package sqlite;

import java.sql.*;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		method();
	}

	public static void method() {
		Connection conn = null;
		Statement stat = null;
		try {
			Class.forName("org.sqlite.JDBC");
			conn = DriverManager.getConnection("jdbc:sqlite:D:/data/sqlite3/jtrac");
			stat = conn.createStatement();
			ResultSet rs = stat.executeQuery("select * from info;");
			while (rs.next()) {
				System.out.println("Ticket_id = " + rs.getString("Ticket_id"));
				System.out.println("Logged_By = " + rs.getString("Logged_By"));
			}
			rs.close();
			conn.close();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

}
