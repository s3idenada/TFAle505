from crud_alunos import criar_aluno, listar_alunos, atualizar_aluno, deletar_aluno

def testar_crud():
    # Teste CREATE
    print("Testando CREATE...")
    aluno_id = criar_aluno("João", 10, "5A")
    print(f"Aluno criado com ID: {aluno_id}")

    # Teste READ
    print("\nTestando READ...")
    alunos = listar_alunos()
    print("Lista de alunos:")
    for aluno in alunos:
        print(aluno)

    # Teste UPDATE
    print("\nTestando UPDATE...")
    atualizar_aluno(aluno_id, nome="João Silva", idade=11)
    print(f"Aluno com ID {aluno_id} atualizado.")

    # Teste DELETE
    print("\nTestando DELETE...")
    deletar_aluno(aluno_id)
    print(f"Aluno com ID {aluno_id} deletado.")

if __name__ == "__main__":
    testar_crud()