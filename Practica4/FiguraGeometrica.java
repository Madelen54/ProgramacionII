package Figura;   
public class FiguraGeometrica {
    double area(double radio){
        return Math.PI * radio * radio;  
    }
    
    int area(int base, int altura){
        return base * altura;
    }
    
    double area(double cateto1, double cateto2){
        return (cateto1 * cateto2) / 2;
    }
    
    double area(double bmayor, double bmenor, double altura){
        return ((bmayor + bmenor) / 2) * altura;  
    }
    
    double area(double lado, int apotema){
        double p = lado * 5;  
        return (p * apotema) / 2;
    }
    
    public static void main(String[] args) {
        FiguraGeometrica f = new FiguraGeometrica();
        
        System.out.println("Area del Circulo: " + f.area(6.3));
        System.out.println("Area del Rectangulo: " + f.area(12, 18));
        System.out.println("Area del Triangulo rectangulo: " + f.area(6.5, 4.3));
        System.out.println("Area del Trapecio: " + f.area(8.0, 6.0, 4.0));
        System.out.println("Area del Pentagono: " + f.area(4.5, 4));  
    }
}
