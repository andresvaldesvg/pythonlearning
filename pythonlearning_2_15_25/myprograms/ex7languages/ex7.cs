using System;

class Program
{
    static void Main()
    {
        Console.Write("What is your favorite food? ");
        string favorite_food = Console.ReadLine();

        if (favorite_food.Equals("Rice Pudding", StringComparison.OrdinalIgnoreCase))
        {
            Console.WriteLine("Yes so nice!");
        }
        else
        {
            Console.WriteLine("Yuck!");
        }

        Console.WriteLine("Thanks for playing.");
    }
}
