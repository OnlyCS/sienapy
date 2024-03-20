/*
 * builtin radix method go brr
 */

import java.util.*;

public class Problem4 {
	static boolean alleq(String s) {
		char[] arr = s.toCharArray();
		for (char c : arr) {
			if (c != arr[0]) {
				return false;
			}
		}

		return true;
	}

	static boolean alleqradix(int i, int b) {
		return alleq(Integer.toString(i, b));
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int i = sc.nextInt();
		boolean any = false;

		for (int b = 2; b <= 16; b++) {
			if (alleqradix(i, b)) {
				System.out.printf("%s Base %s: %s\n", i, b, Integer.toString(i, b));
				any = true;
			}
		}

		if (!any) {
			System.out.println("NO");
		}

		sc.close(); // screw java lint bs
	}
}