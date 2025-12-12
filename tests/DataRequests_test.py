from src.DataEng.DataRequests import DataRequest
def test_DataRequests():
    start = '01/01/2000'
    limit = '01/01/2025'
    response = DataRequest(code=433, start=start, limit=limit)
    assert isinstance(response, list)