import time

from ussd.core import UssdEngine, UssdRequest

if __name__ == "__main__":
    session_id = str(time.time())  # Convert the session ID to a string
    phone_number = input("Enter the user's phone number: ")
    language = "en"

    is_last = False

    while not is_last:
        try:
            message = input(">>>> : ")

            ussd_request = UssdRequest(
                session_id=session_id,
                phone_number=phone_number,
                ussd_input=message,
                language=language,
                journey_name="main_ussd_journey",
                default_http_headers={"Content-Type": "application/json"},
            )

            ussd_engine = UssdEngine(ussd_request=ussd_request)

            dispatched_ussd = ussd_engine.ussd_dispatcher()

            print(getattr(dispatched_ussd, "text", ""))
            # print(dispatched_ussd.status)

            if dispatched_ussd.status is False:
                is_last = True

        except Exception as e:
            print("Error:", str(e))
