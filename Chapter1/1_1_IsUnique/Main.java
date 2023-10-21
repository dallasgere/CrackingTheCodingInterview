import java.util.HashSet;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println(noSet("hello"));
        System.out.println(noSet("helo"));
    }

    public static boolean isUniqueSet(String s) {
        HashSet<Character> set = new HashSet<Character>();
        for (int i = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) {
                return false;
            } else if (!set.contains(s.charAt(i))) {
                set.add(s.charAt(i));
            }
        }

        return true;
    }

    public static boolean noSet(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);

        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] == arr[i + 1]) {
                return false;
            }
        }

        return true;
    }
}