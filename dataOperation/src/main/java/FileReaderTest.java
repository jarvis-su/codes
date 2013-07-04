import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileReaderTest {

	static String fileName1 = "E:\\Document\\L3\\Tickets_NC\\TSGPRD-57413\\Dup cardholder report-0704.csv";
	static String fileName2 = "E:\\Document\\L3\\Tickets_NC\\TSGPRD-57413\\export-0704.csv";
	static String fileName3 = "E:\\Document\\L3\\Tickets_NC\\TSGPRD-57413\\t.csv";

	public static void main(String[] args) {
		String bufferLine;

		String caseId = "";
		String lastname = "";
		String cardholderInsertDate = "";
		String altIdentification = "";
		String[] tmp = null;

		BufferedReader br = null;
		BufferedWriter bwInsertFile = null;

		File file1 = new File(fileName1);

		File wInsertFile = new File(fileName3);
		if (wInsertFile.exists()) {
			wInsertFile.renameTo(new File(fileName3 + System.currentTimeMillis()));
			wInsertFile = new File(fileName3);
		}

		try {
			br = new BufferedReader(new FileReader(file1));
			bufferLine = br.readLine();
			bwInsertFile = new BufferedWriter(new FileWriter(wInsertFile, true));

			while (bufferLine != null) {

				if (bufferLine.startsWith("CASE_NBR")) {
					System.out.println("Title " + bufferLine);
				} else {
					tmp = bufferLine.split(",");
					caseId = tmp[0];
					lastname = tmp[1];
					cardholderInsertDate = tmp[5];
					altIdentification = findAltIdentification(caseId, lastname, cardholderInsertDate);
					String line = bufferLine + altIdentification;
					System.out.println(line);

					bwInsertFile.append(line);
					bwInsertFile.newLine();
					bwInsertFile.flush();
				}
				bufferLine = br.readLine();
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null) {
					br.close();
				}
				if (bwInsertFile != null) {
					bwInsertFile.close();
				}
			} catch (Throwable th) {

			}
		}
	}

	public static String findAltIdentification(String caseId, String lastname, String cardholderInsertDate) {
		File file = new File(fileName2);
		BufferedReader bufferedReader = null;
		String bufferLine;
		String[] tmp = null;
		try {
			bufferedReader = new BufferedReader(new FileReader(file));
			bufferLine = bufferedReader.readLine();
			while (bufferLine != null) {
				tmp = bufferLine.split(",");
				if (caseId.equals(tmp[0]) && lastname.equals(tmp[1]) && cardholderInsertDate.equals(tmp[5])) {
					return tmp[6];
				}
				bufferLine = bufferedReader.readLine();
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return "";
	}
}
