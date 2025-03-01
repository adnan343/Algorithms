import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            String[] arr = s.split(" ");

            if (arr[2].equals("+")) {
                System.out.println(((float) Integer.parseInt(arr[1])) + Integer.parseInt(arr[3]));
            } else if (arr[2].equals("-")) {
                System.out.println((float) Integer.parseInt(arr[1]) - Integer.parseInt(arr[3]));
            } else if (arr[2].equals("*")) {
                System.out.println((float) Integer.parseInt(arr[1]) * Integer.parseInt(arr[3]));
            } else if (arr[2].equals("/")) {
                System.out.println((float) Integer.parseInt(arr[1]) / Integer.parseInt(arr[3]));
            }

        }
    }
}
