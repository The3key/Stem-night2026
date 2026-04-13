import java.util.Scanner;

public class BasicCalculator {

    public static void main(String[] args) {

        double num1;
        double num2;
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the numbers:");
        num1 = sc.nextDouble();
        num2 = sc.nextDouble();

        System.out.println(" DO SOMETHING!! (+, -, *, /)");
        char operator = sc.next().charAt(0);

        double result;
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;

            case '-':
                result = num1 - num2;
                break;

            case '*':
                result = num1 * num2;
                break;

            case '/':
                result = num1 / num2;
                break;

            default:
                System.out.println("Invalid operator.");
                return;
        }
        System.out.println(result);
    }
}
