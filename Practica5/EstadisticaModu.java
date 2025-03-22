package Practica2;
/**
 * obtener el promedio y desviacion: Estadistica
 * Programa modular estructurado 
 * @author ESCARLET*
 * 22/03/25
 */

import java.util.Scanner;

public class Estadistica {
    public static int leerEntero() {
        Scanner dato = new Scanner(System.in);
        return dato.nextInt();
    }
    public static float promedio(int[] numeros) {
        int suma = 0;
        for (int i = 0; i < numeros.length; i++) {
            suma += numeros[i]; 
        }
        return (float) suma / numeros.length; 
    }

    
    public static float desviacion(int[] numeros) {
        float p = promedio(numeros); 
        float suma = 0;
        for (int i = 0; i < numeros.length; i++) {
            suma += Math.pow((numeros[i] - p), 2); 
        }
        return (float) Math.sqrt(suma / numeros.length); 
    }

    public static void main(String[] args) {
        System.out.println("ingresa un numero");
        int n = leerEntero(); 
        
        int[] numeros = new int[n]; 
        System.out.println("Ingresa " + n + " números:");
        for (int i = 0; i < n; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = leerEntero(); 
        }
        float promedio = promedio(numeros);
        System.out.println("El promedio es: " + promedio);
        float desviacion = desviacion(numeros);
        System.out.println("La desviación estándar es: " + desviacion);
    }
}
