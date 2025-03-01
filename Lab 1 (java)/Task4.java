import java.util.Scanner;

public class Task4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n;
        long ans;
        long a = sc.nextInt();
        for (long i = 0; i < a; i++) {
            n = sc.nextInt();
            ans = (n * (n + 1) / 2);
            System.out.println(ans);
        }

    }
}
