import java.util.Scanner;


public class Task1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            if (a % 2 == 0) {
                System.out.println(a + " is an Even number.");
            } else {
                System.out.println(a + " is an Odd number.");
            }
        }
    }
}