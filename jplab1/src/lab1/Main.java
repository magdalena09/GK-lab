package lab1;

public class Main {
    public static void main(String[] args) {
        int max = 10, multi, zero = 0;
        for (int i = 1; i <= max; i++) {
            for (int j = 1; j <= max; j++) {
                multi = i * j;
                if (multi<10) {
                    System.out.print(" " + zero + multi + " ");
                }else
                    System.out.print(multi + "  ");
            }
            System.out.println();
        }
    }
}
