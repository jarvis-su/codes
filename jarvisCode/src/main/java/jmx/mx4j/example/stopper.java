package jmx.mx4j.example;

public class stopper {
	public static void main(String[] args) throws Exception {
		Server server = new Server();
		server.shutdown();
	}
}
