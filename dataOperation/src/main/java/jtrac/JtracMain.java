package jtrac;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import utils.DateUtil;

public class JtracMain {
	// TJ Support Time from 8PM to 4AM of next day.
	static final int TJ_SUPPORT_BEGIN = 0;
	static final int TJ_SUPPORT_END = 4;
	static final int TJ_SUPPORT_BEGIN2 = 20;
	static final int TJ_SUPPORT_END2 = 24;

	static final String ECC_L3_GROUP_NAME = "DEV-L3-GROUP(ECC)";
	static final String ECC_L3_ALVIN_NAME = "Tianjin-DEV - Alvin Du";
	static final String ECC_L3_JARVIS_NAME = "Tianjin-DEV - Jarvis Su";
	static final String ECC_TIANJIN = "Tianjin";
	static final String ACCEPTED_COMMENT = "Accepted";

	static final String JTRAC_DATE_FORMAT = "yyyy-MM-dd HH:mm:ss";

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		JtracInfo info = Jtrac.getAndPackJtracInfo("TSGPRD-56552");
		Date openDate = null;
		Date receivedDate = null;
		Date acceptDate = null;
		Date deliveryDate = null;
		Date closedDate = null;
		boolean isSentToTianjin = false;
		boolean isAccepted = false;
		boolean isDelivered = false;
		boolean isClose = false;
		boolean isInHands = false;
		float totalNonWorkingHrs = 0.0f;
		float nonWorkingHoursIn1stAcknowledge = 0.0f;

		float NotInHandsHoursAndNonWorkingHours = 0.0f;
		String justificationOfNonWorkingHrsIn1stAcknowledge = "";
		String JustificationOfNonInHandsHrsAndNonWorkingHrs = "";

		Date dateInHands = null;
		Date dateNotInHands = null;

		SimpleDateFormat sdf = new SimpleDateFormat(JTRAC_DATE_FORMAT);

		for (JtracDetail d : info.getRecords()) {
			int index = info.getRecords().indexOf(d);
			System.out.println("index =" + index);
			if (d.getAssignedTo() == null || "".equals(d.getAssignedTo())) {
				continue;
			}
			try {
				Date date = sdf.parse(d.getTimeStamp());
				// Set open date
				if (index == 0) {
					openDate = date;
				}
				// set received date
				if (!isSentToTianjin && isAssignedToOffshore(d)) {
					receivedDate = date;
					isSentToTianjin = true;
				}

				// set accepted date
				if (!isAccepted
						&& ACCEPTED_COMMENT.equalsIgnoreCase(d.getComment())) {
					acceptDate = date;
					isAccepted = true;
					isInHands = true;
				}
				// Calculate the acknowledge time
				if (isAccepted && nonWorkingHoursIn1stAcknowledge <= 0) {
					totalNonWorkingHrs += calculateNonWorkingHours(
							receivedDate, acceptDate);
					nonWorkingHoursIn1stAcknowledge = totalNonWorkingHrs;
				}

				if (isInHands && isAssignedToOnshore(d)) {
					isInHands = false;
					dateNotInHands = date;
				}

				if (isAccepted && !isInHands && isAssignedToOffshore(d)) {
					isInHands = true;
					float notInHands = calculateDiffHours(dateNotInHands, date);
					System.out.println("dateNotInHands = " + notInHands);
				}

				// if (ECC_L3_GROUP_NAME.equals(d.getAssignedTo())
				// || ECC_L3_ALVIN_NAME.equals(d.getAssignedTo())
				// || ECC_L3_JARVIS_NAME.equals(d.getAssignedTo())) {
				// isInHands = true;
				// dateInHands = date;
				// }

			} catch (ParseException e) {
				e.printStackTrace();
			}
		}
	}

	private static boolean isAssignedToOnshore(JtracDetail d) {
		return d.getAssignedTo().contains("OM")
				|| d.getAssignedTo().contains("AM")
				|| d.getAssignedTo().contains("OPS")
				|| d.getAssignedTo().contains("CE");
	}

	private static boolean isAssignedToOffshore(JtracDetail d) {
		return ECC_L3_GROUP_NAME.equals(d.getAssignedTo())
				|| ECC_L3_ALVIN_NAME.equals(d.getAssignedTo())
				|| ECC_L3_JARVIS_NAME.equals(d.getAssignedTo())
				|| d.getAssignedTo().startsWith(ECC_TIANJIN);
	}

	public static float calculateNonWorkingHours(Date begin, Date end) {
		float hours = 0.0f;
		return hours;
	}

	public static float calculateDiffHours(Date begin, Date end) {
		float hours = 0.0f;
		hours = (float) ((end.getTime() - begin.getTime()) / 1000.0 / 60.0 / 60.0);
		return hours;
	}

}
