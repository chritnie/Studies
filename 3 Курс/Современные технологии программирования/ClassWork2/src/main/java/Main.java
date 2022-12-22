import java.util.ArrayList;

public class Main {

    public static <T> void myGenericMethod(T obj)
    {
        System.out.println(obj.getClass().toGenericString());
    }
    public static void main(String [] args)
    {
        MyGenericClass<ClassA> genericClass = new MyGenericClass<>(new ClassA());
        genericClass.getObj().methodA();
        ArrayList<ClassC> arrayList1 = new ArrayList<>();
        //arrayList1.add(new ClassA());
        //arrayList1.add(new ClassB());
        arrayList1.add(new ClassC());
        arrayList1.add(new ClassD());
        ArrayList<? super ClassD> arr = arrayList1;

        ArrayList<ClassB> arrayList2 = new ArrayList<>();
        arrayList2.add(new ClassB());
        arrayList2.add(new ClassC());
        arrayList2.add(new ClassD());
        ArrayList<? extends ClassB> arr2 = arrayList1;

        myGenericMethod(arr2);

        ArrayList list = new ArrayList();
        list.add("a");
        list.add(new ClassA());
        list.add(new MyGenericClass<ClassD>(new ClassD()));
        list.add(false);
        list.add(2.333333333f);
    }
}
