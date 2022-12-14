import pytest

stub_product_list = [{"name" : "pepsi", "price" : 0.5}, {"name" : "fanta", "price" : 0.6}]
stub_couriers_list = [{"name" : "Bob", "phone" : "07898878891"}, {"name" : "James", "phone" : "0789879923" }]
stub_orders_list = [{"customer_name" : "John", "customer_address" : "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone" : "0789887334", "courier" : "2", 
"status" : "PREPARING", "items" : [1,2,3]},
 {"customer_name" : "Tom", "customer_address" : "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone" : "0789887334", "courier" : "2", 
"status" : "PREPARING", "items" : [1,2,3]}]

def test_create_new_product():
    #arrange
    expected_new_product_name = "coke"
    expected_new_product_price = 0.5

    #act
    def mock_create_new_product():
        stub_product_list.append({"name" : expected_new_product_name, "price" : expected_new_product_price})
    mock_create_new_product()
    actual_name = stub_product_list[2]["name"]
    actual_price = stub_product_list[2]["price"]

    #assert
    assert (actual_name == expected_new_product_name) and (actual_price == expected_new_product_price)

def test_create_new_courier():
    #arrange
    expected_courier_name = "Timothy"
    expected_courier_phone = "0784879527"

    #act
    def mock_create_new_order():
        stub_couriers_list.append({"name" : expected_courier_name, "phone" : expected_courier_phone})
    mock_create_new_order()
    actual_name = stub_couriers_list[2]["name"]
    actual_phone = stub_couriers_list[2]["phone"]

    #assert
    assert (actual_name == expected_courier_name) and (actual_phone == expected_courier_phone)

def test_create_new_order():
    #arrange
    expected_customer_name = "Sakib"
    expected_customer_address = "12 Main Street, LONDON, WH1 2ER"
    expected_customer_phone = "0789347325"
    expected_courier_choice = "2"
    expected_status = "PREPARING"
    expected_product_choices = ["2", "3", "1"]
    expected_order = {"customer_name" : expected_customer_name, "customer_address" : expected_customer_address,
         "customer_phone" : expected_customer_phone,"courier" : expected_courier_choice, "status" : expected_status, "items" : expected_product_choices}

    #act
    def mock_create_new_order():
        order_dict = {"customer_name" : expected_customer_name, "customer_address" : expected_customer_address,
         "customer_phone" : expected_customer_phone,"courier" : expected_courier_choice, "status" : expected_status, "items" : expected_product_choices}
        stub_orders_list.append(order_dict)
    mock_create_new_order()
    actual_order = stub_orders_list[2]

    #assert
    assert expected_order == actual_order