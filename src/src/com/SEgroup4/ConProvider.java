package com.SEgroup4;
import java.sql.*;
public class ConProvider {

	public static Connection getConnection(){
	Connection con=null;
	try{
//		Class.forName("oracle.jdbc.driver.OracleDriver");
//		con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");
                Class.forName("com.mysql.jdbc.Driver");
                con=DriverManager.getConnection("jdbc:mysql://localhost:3306/employee_mailer","root","Shobhnaj173"); 
	}catch(Exception e){System.out.println(e);}
	return con;
    }
}
