package filaB;

/**
 *
 * @author ESCARLET
 */
public class App {
    public static void main(String[] args) {
        MInisterio m1 = new MInisterio();
        MInisterio m2 = new MInisterio("rojo","Estacion Central, Estacion Cementerio, Estacion 16 de Julio");
        
        System.out.println(m1);
        System.out.print(m2);
        m2.eliminarEmpleado(29);
        System.out.print(m2);
        m1.operador(m2, "Ana");
        System.out.println(m1);
        System.out.println(m2); 
        m1.mostrar(m1.menorEdad());
        m1.mostrar(m1.menorSueldo());
    }
    
}
