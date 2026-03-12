import java.util.ArrayList;
import java.util.*;
class Student {
        int id;
        String name;
        int age;
        Student(int id,String name,int age){
            this.id=id;
            this.name=name;
            this.age=age;}
            public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                ArrayList<Student> students = new ArrayList<>();
                while (true) {
                    System.out.println("\nStudent Management System");
                    System.out.println("1 Add student");
                    System.out.println("2 view Student");
                    System.out.println("3 update student");
                    System.out.println("4 delete student");
                    System.out.println("5 exit");
                    System.out.println("enter your choice");
                    int choice = sc.nextInt();

                    if (choice == 1) {
                        System.out.println("enter id:");
                        int id = sc.nextInt();
                        System.out.println("\nenter name:");
                        String name = sc.nextLine();
                        System.out.println("\nenter age:");

                        int age = sc.nextInt();
                        Student s = new Student(id, name, age);
                        students.add(s);
                        System.out.println("Student added succesfully");
                    } else if (choice == 2) {
                        if (students.isEmpty()) {
                            System.out.println("no student found");
                        } else {
                            for (Student s : students) {
                                System.out.println("ID:" + s.id);
                                System.out.println("names:" + s.name);
                                System.out.println("age:" + s.age);
                            }
                        }
                    } else if (choice == 3) {
                        System.out.println("enter the id to updated");
                        int id = sc.nextInt();
                        sc.nextLine();
                        boolean found = false;
                        for (Student s : students) {
                            if (s.id == id) {
                                System.out.println("enter the new name:");
                                s.name = sc.nextLine();
                                System.out.println("enter the new age:");
                                s.age = sc.nextInt();
                                System.out.println("student updated");
                                found = true;
                                break;
                            }
                        }
                        if (!found) {
                            System.out.println("student not found");
                        }
                    } else if (choice == 4) {
                        System.out.println("enter id to delete:");
                        int id = sc.nextInt();
                        boolean removed = false;
                        for (Student s : students) {
                            if (s.id == id) {
                                students.remove(s);
                                System.out.println("Student removed");
                                removed = true;
                                break;
                            }
                        }
                        if (!removed) {
                            System.out.println("student not found");
                        }
                    }
                    if(choice==5){
                        System.out.println("exit");
                        sc.close();
                        break;
                    }
                    else{
                        System.out.println("invalid choice");
                    }
                }
            }
        }
    


