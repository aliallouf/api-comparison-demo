import grpc
import bank_pb2
import bank_pb2_grpc

def run():
    # 1. Open a connection (Channel) to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # 2. Create a 'Stub' (the virtual client)
        stub = bank_pb2_grpc.BankDashboardStub(channel)
        
        # 3. Create the request object
        request = bank_pb2.SummaryRequest(
            user_id="user_1842",
            auth_token="secure_token_abc123"
        )
        
        # 4. INVOKE the service
        try:
            response = stub.GetUserSummary(request)
            print(f"Balance: {response.account_balance} {response.currency}")
            for tx in response.recent_transactions:
                print(f"Transaction: {tx.description} | {tx.amount}")
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()}")

if __name__ == '__main__':
    run()