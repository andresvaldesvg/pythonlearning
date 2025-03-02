public class Ex7 {
    public static void main(String[] args) {
        // Example 1: Simple if statement
        if (5 < 6) {
            System.out.println("Yes, 5 is less than 6");
            System.out.println("Everybody knows that");
            System.out.println("I am a genius");
        }

        // Example 2: If-else statement
        if (10 > 20) {
            System.out.println("This will not be printed");
        } else {
            System.out.println("10 is not greater than 20");
        }

        // Example 3: If-elif-else statement
        int number = 15;
        if (number < 10) {
            System.out.println("Number is less than 10");
        } else if (number == 15) {
            System.out.println("Number is 15");
        } else {
            System.out.println("Number is greater than 10 but not 15");
        }

        // Example 4: Nested if statements
        int age = 18;
        if (age >= 18) {
            System.out.println("You are an adult");
            if (age >= 65) {
                System.out.println("You are a senior citizen");
            } else {
                System.out.println("You are not a senior citizen");
            }
        } else {
            System.out.println("You are not an adult");
        }
    }
}
