from django.shortcuts import render,redirect
from django.contrib import messages
from  tronpy import Tron


from .models import Deposit
# Create your views here.
tron=Tron()
def verify_trx_payment(txid: str):
    """
    Verify TRX on-chain payment sent to your wallet.
    No minimum amount required.
    """
    try:
        tx = tron.get_transaction(txid)
        receipt = tron.get_transaction_info(txid)
    except Exception:
        return {"success": False, "message": "Transaction not found or pending"}

    # Must be SUCCESS in the blockchain
    status = receipt.get("receipt", {}).get("result", "").upper()
    if status != "SUCCESS":
        return {"success": False, "message": "Transaction not confirmed yet"}

    # Extract details
    contract = tx["raw_data"]["contract"][0]
    value = contract["parameter"]["value"]
    if contract["type"] != "TransferContract":
        return {"success": False, "message": "Not a TRX transfer"}


    # Convert to base58 address
    to_addr = tron.to_base58check_address(bytes.fromhex(value["to_address"]))


    amount_trx = value["amount"] / 1_000_000  # just for info

    return {
        "success": True,
        "message": "Payment verified ✅",
        "amount": amount_trx
    }

def deposit(request):
     
    if request.method == "POST":
        amount=request.POST.get("amount")
        txid=request.POST.get("id")
        result = verify_trx_payment(txid)

        if result["success"]:
            messages.success(request,"Transaction processing")
            return redirect("dashboard")
        else:
            messages.error(request,"Verification failed")
            return redirect("deposit")

    return render(request,"deposit.html")