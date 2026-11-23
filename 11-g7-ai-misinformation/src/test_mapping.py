def test_mapping():
    # pants-fire/false/barely-true -> 1, half/mostly/true -> 0
    m={"pants-fire":1,"false":1,"barely-true":1,"half-true":0,"mostly-true":0,"true":0}
    assert m["pants-fire"]==1 and m["true"]==0
    print("PASS binary mapping")
if __name__=="__main__": test_mapping()
