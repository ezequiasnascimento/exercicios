
public class listas {

	public static void main(String[] args) {
		int lista[] = new int[10];
		for(int i=0;i<lista.length;i++) {
			lista[i] = 3*i;
		}
		for(int i:lista) {
			System.out.print(" "+i);
		}
	}

}
