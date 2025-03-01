import java.util.Arrays;
import java.util.Scanner;

public class Task7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[][] arr = new String[n][7];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLine().split(" ");
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j][0].compareTo(arr[j + 1][0]) > 0) {
                    String[] temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                } else if (arr[j][0].compareTo(arr[j + 1][0]) == 0) {
                    if (arr[j][6].compareTo(arr[j + 1][6]) < 0) {
                        String[] temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i][0] + " " + arr[i][1] + " " + arr[i][2] + " " + arr[i][3] + " " + arr[i][4] + " " + arr[i][5] + " " + arr[i][6]);
        }
    }
}
