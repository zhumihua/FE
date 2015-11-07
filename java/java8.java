//////////////////////////////JAVA 8//////////////////////////////

// lambda expressions
processElements(LIST, element->element.getGender()==Persion.Sex.MALE,
	element->element.getEmailAddress(),
	email->syso(email))
// Aggregate operations with Lambda Expression
LIST.stream().filter(
      element -> element.getGender() == Person.Sex.MALE
	).map(element -> element.getEmailAddress()).forEach(email->syso(email));
stream() filter() map() forEach()

//Example 1
public static <X, Y> void processElements(
    Iterable<X> source,
    Predicate<X> tester,
    Function <X, Y> mapper,
    Consumer<Y> block) {
    for (X p : source) {
        if (tester.test(p)) {
            Y data = mapper.apply(p);
            block.accept(data);
        }
    }
}
processElements(
    roster,
    p -> p.getGender() == Person.Sex.MALE
        && p.getAge() >= 18
        && p.getAge() <= 25,
    p -> p.getEmailAddress(),
    email -> System.out.println(email)
);


//Example 2
public class Calculator {
  
    interface IntegerMath {
        int operation(int a, int b);   
    }
  
    public int operateBinary(int a, int b, IntegerMath op) {
        return op.operation(a, b);
    }
 
    public static void main(String... args) {
    
        Calculator myApp = new Calculator();
        IntegerMath addition = (a, b) -> a + b;
        IntegerMath subtraction = (a, b) -> a - b;
        System.out.println("40 + 2 = " +
            myApp.operateBinary(40, 2, addition));
        System.out.println("20 - 10 = " +
            myApp.operateBinary(20, 10, subtraction));    
    }
}

/*
Processing data with Java SE 8 Streams
http://www.oracle.com/technetwork/articles/java/ma14-java-se-8-streams-2177646.html
http://www.oracle.com/technetwork/articles/java/architect-streams-pt2-2227132.html
*/
// Aggregate operation expression:
double average = roster
    .stream()
    .filter(p -> p.getGender() == Person.Sex.MALE)
    .mapToInt(Person::getAge)
    .average()
    .getAsDouble();

List<Integer> transactionsIds = 
    transactions.stream()
                .filter(t -> t.getType() == Transaction.GROCERY)
                .sorted(comparing(Transaction::getValue).reversed())
                .map(Transaction::getId)
                .collect(toList());

List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8);
List<Integer> twoEvenSquares = 
    numbers.stream()
           .filter(n -> {
                    System.out.println("filtering " + n); 
                    return n % 2 == 0;
                  })
           .map(n -> {
                    System.out.println("mapping " + n);
                    return n * n;
                  })
           .limit(2)
           .collect(toList());

distinct: Returns a stream with unique elements (according to the implementation of equals for a stream element)
limit(n): Returns a stream that is no longer than the given size n
skip(n): Returns a stream with the first n number of elements discarded 

boolean expensive =
    transactions.stream()
                .allMatch(t -> t.getValue() > 100);

 transactions.stream()
              .filter(t -> t.getType() == Transaction.GROCERY)
              .findAny()
              .ifPresent(System.out::println);

List<String> words = Arrays.asList("Oracle", "Java", "Magazine");
 List<Integer> wordLengths = 
    words.stream()
         .map(String::length)
         .collect(toList());

//reduce: sum of the array : 0 is the initial value   
int sum = numbers.stream().reduce(0, (a, b) -> a + b);
int product = numbers.stream().reduce(1,(a,b) -> a*b);
int product = numbers.stream().reduce(1, Integer::max);

int statement = 
    transactions.stream()
                .map(Transaction::getValue)
                .sum(); // error since Stream has no sum method
int statementSum = 
    transactions.stream()
                .mapToInt(Transaction::getValue)
                .sum(); // works!

//range(10,30) exclusive 10 and 13, rangeClosed(10,30) include 10 and 30
IntStream oddNumbers = 
    IntStream.rangeClosed(10, 30)
             .filter(n -> n % 2 == 1);

 // Accumulate names into a List
     List<String> list = people.stream().map(Person::getName).collect(Collectors.toList());

     // Accumulate names into a TreeSet
     Set<String> set = people.stream().map(Person::getName).collect(Collectors.toCollection(TreeSet::new));

     // Convert elements to strings and concatenate them, separated by commas
     String joined = things.stream()
                           .map(Object::toString)
                           .collect(Collectors.joining(", "));

     // Compute sum of salaries of employee
     int total = employees.stream()
                          .collect(Collectors.summingInt(Employee::getSalary)));

     // Group employees by department
     Map<Department, List<Employee>> byDept
         = employees.stream()
                    .collect(Collectors.groupingBy(Employee::getDepartment));

     // Compute sum of salaries by department
     Map<Department, Integer> totalByDept
         = employees.stream()
                    .collect(Collectors.groupingBy(Employee::getDepartment,
                                                   Collectors.summingInt(Employee::getSalary)));

     // Partition students into passing and failing
     Map<Boolean, List<Student>> passingFailing =
         students.stream()
                 .collect(Collectors.partitioningBy(s -> s.getGrade() >= PASS_THRESHOLD));


// create stream
Stream<Integer> numbersFromValues = Stream.of(1, 2, 3, 4);
int[] numbers = {1, 2, 3, 4};
IntStream numbersFromArray = Arrays.stream(numbers);

//numberOfLines in a file
long numberOfLines = 
    Files.lines(Paths.get(“yourFile.txt”), Charset.defaultCharset())
         .count();

//infinite stream
Stream<Integer> numbers = Stream.iterate(0, n->n+10);
numbers.limit(5).forEach(System.out::println); 

//flatMap()
Stream<String> words = Stream.of("Java", "Magazine", "is", 
     "the", "best");

Map<String, Long> letterToCount =
           words.map(w -> w.split(""))
                                   .flatMap(Arrays::stream)
                                   .collect(groupingBy(identity(), counting()));

