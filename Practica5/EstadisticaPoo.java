package practica2poo;
/**
 * obtener el promedio y desviacion: Estadistica
 * Programa POO
 * @author ESCARLET*
 * 22/03/25
 */
import java.util.Scanner;
public class Estadistica1 {
	private int[] numeros;
	public Estadistica1(int[] numeros){
		this.numeros=numeros;
	}
	public float promedio() {
		int suma=0;
		for (int i=0;i<numeros.length;i++) {
			suma+=numeros[i];
		}
		return suma/numeros.length;
	}
	public float desviacion() {
		float p=promedio();
		float suma=0;
		for (int i=0;i<numeros.length;i++){
			 suma += Math.pow((numeros[i] - p), 2); 
		}
		return (float) Math.sqrt(suma / numeros.length); 
	}

	public static void main(String[] args) {
		Scanner dato=new Scanner(System.in);
		System.out.print("ingresa la cantidad de numeros: ");
		int n=dato.nextInt();
		int []numeros=new int[n];
		for (int i=0;i<n;i++) {
			System.out.println("ingresa el numero "+(i+1)+".");
			numeros[i]=dato.nextInt();
		}
		Estadistica1 list=new Estadistica1(numeros);
		System.out.println("el promedio es de "+list.promedio());
		System.out.println("la desviacion estandar es de "+list.desviacion());
		}

}
