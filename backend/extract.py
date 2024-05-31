from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
from dotenv import load_dotenv
load_dotenv()
def imageExtraction(url):
    try:
        endpoint = os.getenv("ENDPOINT")
        key = os.getenv("KEY")
        document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
        poller=document_analysis_client.begin_analyze_document("prebuilt-layout",url)
        result = poller.result()
        board=[]
        for table_idx, table in enumerate(result.tables):
            tp=[]   
            for cell in table.cells:
                tp.append(cell.content.encode("utf-8"))
            board.append(tp)
    except Exception as e:
        return []
    tp=[]
    for i in range(0,81,9):
        tp.append(board[0][i:i+9])
    res=[]
    for i in tp:
        e=[]
        for j in i:
            dig=j.decode().replace(":unselected:",'').replace(":selected:",'').strip()
            if dig.isdigit():
                e.append(int(dig))
            else:
                e.append('')
        res.append(e)
    return res