package jmx.mx4j.example; 

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.Reader;
import java.net.Socket;

import javax.management.MBeanServer;
import javax.management.MBeanServerFactory;
import javax.management.ObjectName;

import mx4j.tools.config.ConfigurationLoader;

public class Server {
    public void startup() throws Exception {
        MBeanServer server = MBeanServerFactory.newMBeanServer();
        ConfigurationLoader loader = new ConfigurationLoader();

        server.registerMBean(loader, ObjectName.getInstance("config:service=loader"));
        Reader reader = new BufferedReader(new FileReader("config/mx4j/mx4jConfig.xml"));
        
        loader.startup(reader);
        reader.close();
        System.out.println("Start the server successfully!");
    }
    public void shutdown() throws Exception {
          String shutdownCommand = "shutdown";
          Socket socket = new Socket("127.0.0.1", 9999);
          socket.getOutputStream().write(shutdownCommand.getBytes());
          socket.close();
    }
}

