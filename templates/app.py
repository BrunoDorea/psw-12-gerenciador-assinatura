import __init__
from views.view import SubscriptionService
from models.database import engine
from models.model import Subscription
from datetime import datetime
from decimal import Decimal


class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)

    def start(self):
        while True:
            print(
                """
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [0] -> Sair
            """
            )

            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_value()
            elif choice == 4:
                self.subscription_service.gen_chart()
            elif choice == 5:
                pass
                # TODO: Implementar método pay na interface
            else:
                break

    def add_subscription(self):
        empresa = input("Digite o nome da empresa: ")
        site = input("Digite o site da empresa: ")
        data_assinatura = datetime.strptime(
            input("Digite a data de assinatura: "), "%d/%m/%Y"
        )
        valor = Decimal(input("Digite o valor da assinatura: "))

        subscription = Subscription(
            empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor
        )

        self.subscription_service.create(subscription)
        print("Assinatura adicionada com sucesso.")

    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        print("Selecione uma assinatura para remover: ")

        # TODO: Quando remover a assinatura, remover todos os pagamentos dela.

        for i in subscriptions:
            print(f"[{i.id}] -> {i.empresa}")

        choice = int(input("Digite o número da assinatura: "))
        self.subscription_service.delete(choice)
        print("Assinatura removida com sucesso!")

    def total_value(self):
        print(
            f"O valor total mensal das assinaturas é: R$ {self.subscription_service.total_value()}"
        )


if __name__ == "__main__":
    UI().start()
