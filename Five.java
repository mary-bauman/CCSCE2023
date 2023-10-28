import java.util.*;

public class Five {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        int max = 0;
        int solution = 0;
        for (int i = 0; i < num; i++) {
            String d = sc.nextLine();
            String[] data = d.split(" ");
            int[] cards = new int[201];
            for(int j = 0; j < data.length; j++) {
                int val = Integer.parseInt(data[j]);
                for(int k = 1; k <= val; k ++) {
                    cards[k]+=k;
                    if(cards[k] > max) {
                        max = cards[k];
                        solution = k;
                    }
                    if(cards[k] == max) {
                        if(k > solution) {
                            solution = k;
                        }
                    }
                }
            }
            System.out.println(solution);
            max = 0;
            solution = 0;
        }
    }
}
