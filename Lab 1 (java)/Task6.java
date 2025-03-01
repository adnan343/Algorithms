import java.util.Arrays;
import java.util.Scanner;

public class Task6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        String[] arr1 = s1.split(" ");
        String[] arr2 = s2.split(" ");
        int numSwap = 0;
        for (int i = 0; i < arr2.length; i++) {
            String min = arr2[i];
            int minIndex = i;
            for (int j = i; j < arr2.length; j++) {
                if (Integer.parseInt(arr2[j]) > Integer.parseInt(min)) {
                    min = arr2[j];
                    minIndex = j;
                }
                if (Integer.parseInt(arr2[j]) == Integer.parseInt(min)) {
                    if (Integer.parseInt(arr1[minIndex]) > Integer.parseInt(arr1[j])) {
                        min = arr2[j];
                        minIndex = j;
                    }
                }
            }
            if (minIndex != i) {
                arr2[minIndex] = arr2[i];
                String temp = arr1[minIndex];
                arr1[minIndex] = arr1[i];
                arr1[i] = temp;
                arr2[i] = min;
                numSwap++;
            }

        }
        System.out.println("Minimum swaps: " + numSwap);
        for (int i = 0; i < arr2.length; i++) {
            System.out.print("ID: " + arr1[i] + " Mark: " + arr2[i] + "\n");
        }
    }


}
