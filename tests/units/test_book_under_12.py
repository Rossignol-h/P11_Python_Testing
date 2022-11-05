from conftest import get_data, post_request


def test_purchase_more_in_one_step(client, fixture):
    """
        GIVEN a connected secretary's club has 15 points.
        WHEN this secretary types: 13 places to book for 
            a competition who has 20 places available,
        THEN an error message displays, with status code:400 BAD REQUEST.
    """
    data = get_data(fixture, 13)
    response = post_request(client, data)

    assert response.status_code == 400
    assert b'Sorry, you can&#39;t book more than 12 places !' in response.data


def test_purchase_more_in_two_step(client, fixture):
    """
        GIVEN a connected secretary's club has 15 points.
        FIRST REQUEST :
            WHEN this secretary types: 10 places to book for 
            a competition who has 20 places available,
            THEN places are pruchased.

        SECOND REQUEST :
            WHEN this secretary types: 3 places to book for the same competition,
            THEN an error message displays, with status code:400 BAD REQUEST.
    """
    data = get_data(fixture, 10)
    response = post_request(client, data)

    data2 = get_data(fixture, 3)
    response = post_request(client, data2)

    assert response.status_code == 400
    assert b"Sorry, you have already booked places, for this competition" in response.data
