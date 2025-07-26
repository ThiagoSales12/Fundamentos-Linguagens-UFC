using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;

class ProcessamentoConcorrente
{
    static void Tarefa(int id)
    {
        Console.WriteLine($"Iniciando tarefa {id} na thread {Thread.CurrentThread.ManagedThreadId}");
        Thread.Sleep(1000); 
        Console.WriteLine($"Finalizando tarefa {id} na thread {Thread.CurrentThread.ManagedThreadId}");
    }

    static void ExecutarSequencial(int n)
    {
        for (int i = 1; i <= n; i++)
        {
            Tarefa(i);
        }
    }

    static void ExecutarConcorrente(int n)
    {
        List<Thread> threads = new List<Thread>();

        for (int i = 1; i <= n; i++)
        {
            int tarefaId = i; 
            Thread t = new Thread(() => Tarefa(tarefaId));
            threads.Add(t);
            t.Start();
        }

        foreach (var t in threads)
        {
            t.Join();
        }
    }

    static void Main()
    {
        int numeroTarefas = 5;

        Stopwatch sw = new Stopwatch();

        Console.WriteLine("=== Execução Sequencial ===");
        sw.Start();
        ExecutarSequencial(numeroTarefas);
        sw.Stop();
        Console.WriteLine($"Tempo total sequencial: {sw.ElapsedMilliseconds} ms\n");

        Console.WriteLine("=== Execução Concorrente ===");
        sw.Restart();
        ExecutarConcorrente(numeroTarefas);
        sw.Stop();
        Console.WriteLine($"Tempo total concorrente: {sw.ElapsedMilliseconds} ms");
    }
}
