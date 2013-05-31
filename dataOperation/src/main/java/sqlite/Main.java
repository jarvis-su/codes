package sqlite;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
//		method();
		String formatStr ="yyyy-dd-MM HH:mm:ss";
		SimpleDateFormat sdf = new SimpleDateFormat(formatStr);
		String beginStr ="2013-05-30 15:31:57";
		String endStr = "2013-06-03 15:31:57";
		Date beginDate = new Date();
		Date endDate = new Date();
		try {
			beginDate = sdf.parse(beginStr);
			endDate = sdf.parse(endStr);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		System.out.println(sdf.format(beginDate));
		System.out.println(sdf.format(endDate));
		getNonWorkingHours(beginDate,endDate);
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
	
	public static void getNonWorkingHours(Date begin, Date end){
		Calendar c = Calendar.getInstance();
		c.setTime(begin);
		
	}

}
