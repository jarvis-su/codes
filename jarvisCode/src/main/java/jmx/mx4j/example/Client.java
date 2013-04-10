/**
 * 
 */
package jmx.mx4j.example;

import java.util.Map;

import javax.management.MBeanInfo;
import javax.management.MBeanOperationInfo;
import javax.management.MBeanServerConnection;
import javax.management.ObjectName;
import javax.management.remote.JMXConnector;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXServiceURL;

/**
 * @author 30110353
 *
 */
public class Client {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		JMXServiceURL address = new JMXServiceURL("service:jmx:rmi://localhost:1316/jndi/rmi://localhost:1099/jmx");
        Map creationEnv = null;
        JMXConnector connector = JMXConnectorFactory.newJMXConnector(address, creationEnv);
       
        Map connectionEnv = null;
        connector.connect(connectionEnv);
        
        MBeanServerConnection serverConnection = connector.getMBeanServerConnection();
        ObjectName name = ObjectName.getInstance("services:type=my-remote");
        MBeanInfo mbInfo = serverConnection.getMBeanInfo(name);
        MBeanOperationInfo[] operationInfo = mbInfo.getOperations();
        
        for (int i = 0; i < operationInfo.length; i++) {
            System.out.println(operationInfo[i].getName());
        }
        
        serverConnection.invoke(name, "sayHello", new Object[] {"Tower He"}, new String[] {"java.lang.String"});
	}

}
