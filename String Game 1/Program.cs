using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Read first line - the number of test cases t,  1 <= t <= 1000 */
            bool isOke;
            int t;
            Console.Write("Type the number of cases: ");
            string input = Console.ReadLine();
            isOke = int.TryParse(input, out t);
            if (!isOke || t < 1 || t > 1000) {
                Console.WriteLine("Wrong input");
                return;
            }

            /* Read the input cases of length s,  1 <= |s| <= 50 */
            Console.WriteLine("\nInput (cases of length s, 1 <= |s| <= 50):");
            string[] cases = new string[t];
            for (int i = 0; i < t; i++) {
                do {
                    cases[i] = Console.ReadLine();
                } while (cases[i].Length < 1 || cases[i].Length > 50);
            }

            Console.WriteLine("\nOutput:");

            /* Start the timer */
            var watch = new System.Diagnostics.Stopwatch();
            watch.Start();

            /* Prepare the output */
            System.Text.StringBuilder sb = new System.Text.StringBuilder();
            foreach (string item in cases) {
                int turn = 1;
                foreach (char ch in item) {
                    if (turn % 2 == 1) {
                        if (ch == 'a')
                            sb.Append('b');
                        else
                            sb.Append('a');
                    } else {
                        if (ch == 'z')
                            sb.Append('y');
                        else
                            sb.Append('z');
                    }
                    turn++;
                }
                Console.WriteLine(sb.ToString());
                sb.Clear();
            }

            /* Stop the timer */
            watch.Stop();
            Console.WriteLine($"\nExecution Time: {watch.ElapsedMilliseconds} ms");

            /* Memory used */
            System.Diagnostics.Process proc = System.Diagnostics.Process.GetCurrentProcess();
            long memoryUsed = proc.PrivateMemorySize64;
            Console.WriteLine($"Memory used: {memoryUsed} bytes = {memoryUsed / 1000000} megabytes");
        }
    }
}