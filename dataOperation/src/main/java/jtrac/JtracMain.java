package jtrac;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class JtracMain {
	// TJ Support Time from 8PM to 4AM of next day.
	static final int TJ_SUPPORT_BEGIN = 0;
	static final int TJ_SUPPORT_END = 4;
	static final int TJ_SUPPORT_BEGIN2 = 20;
	static final int TJ_SUPPORT_END2 = 24;

	static final String ECC_L3_GROUP_NAME = "DEV-L3-GROUP(ECC)";
	static final String ECC_L3_ALVIN_NAME = "Tianjin-DEV - Alvin Du";
	static final String ECC_L3_JARVIS_NAME = "Tianjin-DEV - Jarvis Su";

	static final String JTRAC_DATE_FORMAT = "yyyy-dd-MM HH:mm:ss";
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		JtracInfo info = Jtrac.getAndPackJtracInfo("TSGPRD-56552");
		Date openDate = null;
		Date receivedDate = null;
		boolean isSentToTianjin = false;
		Date acceptDate = null;
		boolean isAccepted = false;
		Date deliveryDate = null;
		boolean isDelivered = false;
		Date closedDate = null;
		boolean isClose = false;
		float nonWorkingHoursIn1stAcknowledge = 0.0f;
		float NotInHandsHoursAndNonWorkingHours = 0.0f;
		String JustificationOfNonWorkingHrsIn1stAcknowledge = "";
		String JustificationOfNonInHandsHrsAndNonWorkingHrs = "";

		SimpleDateFormat sdf = new SimpleDateFormat(JTRAC_DATE_FORMAT);

		for (JtracDetail d : info.getRecords()){
			if (!isSentToTianjin && (ECC_L3_GROUP_NAME.equals(d.getAssignedTo())||ECC_L3_ALVIN_NAME.equals(d.getAssignedTo())||ECC_L3_JARVIS_NAME.equals(d.getAssignedTo()))){
				try {
					receivedDate = sdf.parse(d.getTimeStamp());
				} catch (ParseException e) {
					e.printStackTrace();
				}
				isSentToTianjin = true;
			}

		}

		System.out.println(info.getRecords().toArray());

	}

}
