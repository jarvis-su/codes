import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import jtrac.JtracMain;

public class Test {
	public static void main(String[] t) {
		JtracMain main = new JtracMain();
		String formatStr = "yyyy-MM-dd HH:mm:ss";
		SimpleDateFormat sdf = new SimpleDateFormat(formatStr);
		String beginStr = "2013-06-02 19:00:00";
		String endStr = "2013-06-03 19:00:00";
		Date beginDate = new Date();
		Date endDate = new Date();
		try {
			beginDate = sdf.parse(beginStr);
			endDate = sdf.parse(endStr);

			float hours = (float) ((endDate.getTime() - beginDate.getTime()) / 1000.0 / 60.0 / 60.0);
			System.out.println(hours);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		System.out.println(sdf.format(beginDate));
		System.out.println(sdf.format(endDate));

//		Calendar c = Calendar.getInstance();
//		c.set(Calendar.HOUR_OF_DAY, 20);
//		System.out.println(sdf.format(c.getTime()));
		float te  = main.calculateNonWorkingHours(beginDate, endDate);

		System.out.println(te);
	}

}
