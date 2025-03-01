import java.util.Scanner;


public class Task3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();

        String s1 = sc.nextLine();
        String[] arr1 = s1.split(" ");

        for (int i = k - 1; i >= 0; i--) {
            System.out.print(arr1[i] + " ");
        }

    }

}

// The solution exceeds time limit, however same approach with python gets accepted and a code with two non-nested loops gets accepted in cpp