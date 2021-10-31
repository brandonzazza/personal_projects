
public class AwesomeJavaprogram {

	public static void main(String[] args) {
		int myInt = 7;
		/* Created an int called myInt which is then printed out*/
		System.out.println(myInt);
		System.out.println(myInt+3);
		/* Created a string called Hello World which is then printed out*/
		String mystring = "Hello World";
		System.out.println(mystring);
		/*  This will call another function*/
		burp();
		
		System.out.println(printName("Brandon"));
		
	}
	private static void burp() {
		System.out.println("Buuurrrp");
	}	
	private static String printName(String name) {
		return "My Name is " + name;
	}
}
