package jtrac;

public class JtracMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		JtracInfo info = Jtrac.getAndPackJtracInfo("TSGPRD-56552");
		System.out.println(info.getRecords().toArray());
	}

}
