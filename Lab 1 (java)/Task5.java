import java.util.Scanner;

public class Task5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] arr = sc.nextLine().split(" ");

        for (int i = 0; i < n; i++) {
            boolean flag = false;
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (Integer.parseInt(arr[j]) > Integer.parseInt(arr[j + 1])) {
                    flag = true;
                    int temp = Integer.parseInt(arr[j]);
                    arr[j] = arr[j + 1];
                    arr[j + 1] = String.valueOf(temp);
                }
            }
            if (!flag) {
                break;
            }

        }
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}