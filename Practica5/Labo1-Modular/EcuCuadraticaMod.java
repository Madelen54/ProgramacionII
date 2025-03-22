/**
 * obtener la solucion de una ecuacion cuadratica
 * Programa modular estructurado 
 * @author ESCARLET*
 * 22/03/25
 */

import java.util.Scanner;

public class EcuCuadraticas {
	public static int leerEntero(){
		Scanner dato= new Scanner(System.in);
	    return dato.nextInt();
	}
	public static double getDiscriminante(int a , int b, int c) {
		return Math.pow(b, 2) - 4 * a * c;
		}
	public static String getRaiz1(int a, int b ) {
		double x = -b / (2.0 * a);
        return String.format("La ecuación tiene una solución real: x = %.2f", x);

	}
	public static String getRaiz2(int a, int b , int c) {
		double d=getDiscriminante(a,b,c);
		double x1 = (-b + Math.sqrt(d)) / (2.0 * a);
        double x2 = (-b - Math.sqrt(d)) / (2.0 * a);
        return String.format("La ecuación tiene dos soluciones reales: x1 = %.2f, x2 = %.2f", x1, x2);
	}
    public static void main(String[] args) {
        System.out.println("Ingresa el valor de a: ");
        int a = leerEntero();
        System.out.println("Ingresa el valor de b: ");
        int b = leerEntero();
        System.out.println("Ingresa el valor de c: ");
        int c = leerEntero();
        double discriminante = getDiscriminante(a, b, c);
        
        if (discriminante < 0) {
            System.out.println("La ecuación no tiene soluciones reales.");
        } else if (discriminante == 0) {
            System.out.println(getRaiz1(a, b)); 
        } else {
            System.out.println(getRaiz2(a, b, c));  
        }
    }
}
