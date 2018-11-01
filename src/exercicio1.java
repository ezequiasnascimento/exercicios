
import java.util.Scanner;

public class exercicio1 {
	public static void main(String[] args) {
		int lista[] = new int[10];
		Scanner ler = new Scanner(System.in);
		for(int x=0;x<10;x++) {
			System.out.println("N: ?");
			lista[x] = ler.nextInt();
		}
		for(int i:lista) {
			System.out.print(" "+i*i);
		}
		}
	}

