public class MyGenericClass2 <T extends ClassD>{
    private T obj;
    MyGenericClass2(T obj)
    {
        this.obj = obj;
    }
    public T getObj()
    {
        obj.methodA();
        obj.methodB();
        obj.methodC();
        obj.methodD();

        return obj;
    }
}
