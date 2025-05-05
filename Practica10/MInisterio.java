package filaB;
public class MInisterio {
    private String nombre;
    private String direccion;
    private int nroEmpleados;
    private String [][]empleados=new String [3][100];
    private int[] edades=new int[100];
    private double[] sueldos=new double[100];
    public MInisterio(){
        this.nombre="";
        this.direccion="";
        this.nroEmpleados=0;
        
    }
    public MInisterio(String nombre, String direccion){
        this.nombre=nombre;
        this.direccion=direccion;
        this.empleados[0][0] = "pedro";
        this.empleados[1][0] = "rojas";
        this.empleados[2][0] = "luna";
        this.empleados[0][1] = "lucy";
        this.empleados[1][1] = "sosa";
        this.empleados[2][1] = "rios";
        this.empleados[0][2] = "ana";
        this.empleados[1][2] = "perez";
        this.empleados[2][2] = "rojas";
        this.empleados[0][3] = "saul";
        this.empleados[1][3] = "arce";
        this.empleados[2][3] = "calle";
        this.edades[0] = 35;
        this.edades[1] = 43;
        this.edades[2] = 26;
        this.edades[3] = 29;
        this.sueldos[0] = 2500;
        this.sueldos[1] = 3250;
        this.sueldos[2] = 2700;
        this.sueldos[3] = 2500;
        this.nroEmpleados = (this.empleados).length+1;
    }
    @Override
    public String toString() {
        String salida = "";
        for (int i=0; i<this.nroEmpleados;i++){
            salida=salida+("Nombre: "+this.empleados[0][i]+" Paterno: "+this.empleados[1][i]+" Materno: "+this.empleados[2][i]
                    +" Edad: "+this.edades[i]+" Sueldo: "+this.sueldos[i])+"\n";
        }
        return "Ministerio" + " nombre=" + nombre + ", direccion=" + direccion + ", nroEmpleados=" + nroEmpleados
                +"\n"+salida ;
    }
    public void eliminarEmpleado(int x){
        for (int i=0; i<this.nroEmpleados;i++){
            if(this.edades[i] == x){
                for (int j =i; j<this.nroEmpleados;j++){
                    this.empleados[0][j]=this.empleados[0][j+1];
                    this.empleados[1][j]=this.empleados[1][j+1];
                    this.empleados[2][j]=this.empleados[2][j+1];
                    this.edades[j] = this.edades[j+1];
                    this.sueldos[j] = this.sueldos[j+1];
                }
                this.nroEmpleados --;
            }
        }
    }
    public void operador(MInisterio m, String x){
        int pos = 0; 
        for(int i = 0; i<m.nroEmpleados;i++){
            if(m.empleados[0][i].equals(x)){
                pos = i;
                break;
            }
        }
        this.empleados[0][this.nroEmpleados] = m.empleados[0][pos];
        this.empleados[1][this.nroEmpleados] = m.empleados[1][pos];
        this.empleados[2][this.nroEmpleados] = m.empleados[2][pos];
        this.edades[this.nroEmpleados] = m.edades[pos];
        this.sueldos[this.nroEmpleados] = m.sueldos[pos];
        this.nroEmpleados ++;
        for (int j =pos; j<m.nroEmpleados;j++){
            m.empleados[0][j]=m.empleados[0][j+1];
            m.empleados[1][j]=m.empleados[1][j+1];
            m.empleados[2][j]=m.empleados[2][j+1];
            m.edades[j] = m.edades[j+1];
            m.sueldos[j] = m.sueldos[j+1];
        }
        m.nroEmpleados --; 
    }
    
    public int menorEdad(){
        int menor = 9999999;
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.edades[i] < menor){
                menor = this.edades[i];
            }
        }
        return menor;
    }
    public double menorSueldo(){ 
        double menor = 9999999;
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.sueldos[i] < menor){
                menor = this.sueldos[i];
            }
        }
        return menor;
    }
    
    public void mostrar(int x){
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.edades[i] == x){
                System.out.println(("Nombre: "+this.empleados[0][i]+" Paterno: "+this.empleados[1][i]+" Materno: "+this.empleados[2][i]
                    +" Edad: "+this.edades[i]+" Sueldo: "+this.sueldos[i])+"\n");
            }
        }
    }
    public void mostrar(double x){
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.sueldos[i] == x){
                System.out.println(("Nombre: "+this.empleados[0][i]+" Paterno: "+this.empleados[1][i]+" Materno: "+this.empleados[2][i]
                    +" Edad: "+this.edades[i]+" Sueldo: "+this.sueldos[i])+"\n");
            }
        }
    }
   
}
