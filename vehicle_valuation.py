"""
    NOTE:
        - This module (car_valuation.py) is used for
          getting vehicle information with the UKVD
          API and for calculating vehicle Kerb Weight
          againt an agents price per kg.

    =================================================

    Dependencies:
        requests - ($ pip install requests).
"""

# Dependencies for UKVD API imports.
import requests


class GetVehicleInformation:
    """
        NOTE:
            - The GetVehicleInformation class contains functions
              for getting vehicle information from the UKVD 
              (https://uk1.ukvehicledata.co.uk) API.

        Functions:
            # vehicle_image()
            # vehicle_details()
            -----------------------------------------------
            vehicle_image():
                - This function (vehicle_image()) is used to get
                  the vehicle's image.

            vehicle_details():
                - This function (vehicle_details()) is used 
                  to get all the nescessary vehicle data from 
                  the UKVD API.
    """
    
    def __init__(self, r):
        """
            @params
                r - To pass in a request object for the UKVD API 
                    Data Package.
        """
        self.r = r


    def vehicle_image(self):
        """
            @returns
                image_url - returns the vehicle image url.
        """
        response_json = self.r.json()
        # Get vehicle image from UKVD API.
        print("\n\n\nVehicle Image Details: {0}\n\n\n".format(str(response_json)))
        # Vehicle image url initializer.
        image_url = ""
        try:
            image_url = response_json['Response']['DataItems']['VehicleImages']['ImageDetailsList'][0]['ImageUrl']
        except KeyError:
            pass
        return image_url


    def vehicle_details(self):
        """            
            @returns
                data_store - returns a dictionary object containing
                            vehicle information.
        """
        # Response JSON Object
        response_json = self.r.json()

        # data store dictionary initializer.
        data_store = {}

        # Get vehicle information for valuation from
        # UKVD API.
        print("\n\n\nVehicle Make: {0}\n\n\n".format(str(response_json['Response'])))
        # Set key error intializer.
        key_error = True
        try:
            vehicle_make = response_json['Response']['DataItems']['VehicleRegistration']['Make']
            vehicle_kw = response_json['Response']['DataItems']['TechnicalDetails']['Dimensions']['KerbWeight']
            date_first_reg_uk = response_json['Response']['DataItems']['VehicleRegistration']['DateFirstRegisteredUk']
            date_first_reg = response_json['Response']['DataItems']['VehicleRegistration']['DateFirstRegistered']
            co2 = response_json['Response']['DataItems']['TechnicalDetails']['Performance']['Co2']
            exported = response_json['Response']['DataItems']['VehicleRegistration']['Exported']
            imported = response_json['Response']['DataItems']['VehicleRegistration']['Imported']
            scrapped = response_json['Response']['DataItems']['VehicleRegistration']['Scrapped']
            seating_capacity = response_json['Response']['DataItems']['VehicleRegistration']['SeatingCapacity']
            year_of_manufacture = response_json['Response']['DataItems']['VehicleRegistration']['YearOfManufacture']
            vin_last_5 = response_json['Response']['DataItems']['VehicleRegistration']['VinLast5']
            model = response_json['Response']['DataItems']['VehicleRegistration']['Model']
            color = response_json['Response']['DataItems']['VehicleRegistration']['Colour']
            import_non_eu = response_json['Response']['DataItems']['VehicleRegistration']['ImportNonEu']
            date_scrapped = response_json['Response']['DataItems']['VehicleRegistration']['DateScrapped']
            vehicle_class = response_json['Response']['DataItems']['VehicleRegistration']['VehicleClass']
            engine_number = response_json['Response']['DataItems']['VehicleRegistration']['EngineNumber']
            door_plan_literal = response_json['Response']['DataItems']['VehicleRegistration']['DoorPlanLiteral']
            vrm = response_json['Response']['DataItems']['VehicleRegistration']['Vrm']
            engine_capacity = response_json['Response']['DataItems']['VehicleRegistration']['EngineCapacity']
            driving_axle = response_json['Response']['DataItems']['TechnicalDetails']['General']['DrivingAxle']
            euro_status = response_json['Response']['DataItems']['TechnicalDetails']['General']['EuroStatus']
            fuel_type = response_json['Response']['DataItems']['VehicleRegistration']['FuelType']
            full_vin = response_json['Response']['DataItems']['VehicleRegistration']['Vin']
            date_exported = response_json['Response']['DataItems']['VehicleRegistration']['DateExported']
            type_approval_category = response_json['Response']['DataItems']['TechnicalDetails']['General']['TypeApprovalCategory']
            number_of_gears = response_json['Response']['DataItems']['SmmtDetails']['NumberOfGears']
            
            # Dictionary (data_store) to store vehicle information.
            data_store["vehicle_make"] = vehicle_make
            data_store["vehicle_kw"] = vehicle_kw
            data_store["date_first_reg_uk"] = date_first_reg_uk
            data_store["date_first_reg"] = date_first_reg
            data_store["co2"] = co2
            data_store["exported"] = exported
            data_store["imported"] = imported
            data_store["scrapped"] = scrapped
            data_store["seating_capacity"] = seating_capacity
            data_store["year_of_manufacture"] = year_of_manufacture
            data_store["vin_last_5"] = vin_last_5
            data_store["model"] = model
            data_store["color"] = color
            data_store["import_non_eu"] = import_non_eu
            data_store["date_scrapped"] = date_scrapped
            data_store["vehicle_class"] = vehicle_class
            data_store["engine_number"] = engine_number
            data_store["door_plan_literal"] = door_plan_literal
            data_store["vrm"] = vrm
            data_store["engine_capacity"] = engine_capacity
            data_store["driving_axle"] = driving_axle
            data_store["euro_status"] = euro_status
            data_store["fuel_type"] = fuel_type
            data_store["full_vin"] = full_vin
            data_store["date_exported"] = date_exported
            data_store["type_approval_category"] = type_approval_category
            data_store["number_of_gears"] = number_of_gears
        except KeyError:
            key_error = False
        
        # Store key error.
        data_store["key_error"] = key_error        
        return data_store


def get_vehicle_image(r):
    response_json = r.json()
    print("\n\n\n{0}\n\n\n".format(str(response_json)))
    


def vehicle_kw_calculation(vehicle_kw, agent_price):
    """
        NOTE:
            - This function (vehicle_kw_calculation()) does a
              calcualtion bewtween the highest per kg an agent 
              is offering and the vehicle's Kerb Weight.

        @params
            vehicle_kw - To pass through a vehicles Kerb Weight.

        @returns
            _result - returns the price offered for the vehicle
                      or returns returns a 'No agents in your postcode'
                      message.
    """
    # Check if vehicle is not a None type if it
    # is set it to 0.
    if vehicle_kw is None:
        vehicle_kw = 0

    _result = ""
    try:
        # Calculate Agent price per kg against
        # the vehicle kerb weight.
        _result = float(vehicle_kw) * float(agent_price)
    except ValueError:
        _result = agent_price
    return _result


class UKVDCarValuation:
    """
        NOTE:
            - The UKVDCarValuation class is for getting
              vehicle information from the UKVD 
              (https://uk1.ukvehicledata.co.uk) API.
              The function's this class (UKVDCarValuation)
              contains is to send and get requests, response
              checks from the mentioned API.

        Functions:
            # set_payload()
            # get_data_package()
            # get_vehicle_image()
            # check_response()
            -----------------------------------------------
            set_payload():
                - To Create a payload.

            get_data_package():
                - To Create a GET request to get the API 
                  Data Package.

            get_vehicle_image():
                - To get the vehicle image.

            check_response():
                - To check the request code if it was
                  successful or not.

    """

    def __init__(self, api_key, data_package, vrm, response_json=""):
        """
            @params
                api_key - To pass in the UKVD API key.
                data_package - To pass in the Data Package
                               you want information from.
                vrm - (Vehicle Registration Mark) To pass in
                      the vehicle registration number.
                response_json - To pass in a json response
                                object which has a default 
                                empty string.
        """
        self.api_key = api_key
        self.data_package = data_package
        self.vrm = vrm
        self.response_json = response_json


    def set_payload(self, package_version=2, nullitems=1):
        """
            @params
                package_version - To pass in a package version
                                  which has 2 as a default.
                nullitems - To pass in a nullitem which has 1
                            as a default.

            @returns
                payload - returns a payload dictionary which 
                          contains all the data needed for the
                          UKVD API.
        """
        # Create payload dictionary.
        payload = {
            "v": package_version, # Package version.
            "api_nullitems": nullitems, # Returns null items.
            "key_vrm": self.vrm, # Vehicle registration mark.
            "auth_apikey": self.api_key # Set the API Key.
        }
        return payload


    def get_data_package(self, payload):
        """
            @params
                payload - To pass in a payload dictionary.

            @returns
                r - returns the request object for the UKVD API 
                    Data Package.
        """
        # Create GET Request (Include payload & headers)
        r = requests.get('https://uk1.ukvehicledata.co.uk/api/datapackage/{}'.format(self.data_package), params = payload)
        return r


    def get_vehicle_image(self, r):
        """
            @params
                r - To pass in a request object for the UKVD API
                    Data Package.
                
            @returns
                v_image - returns the vehicle image.
                ErrorContent - returns the error of the failed 
                               request.

        """
        # Check for a successful response
        if r.status_code == requests.codes.ok:
            vehicle_information = GetVehicleInformation(r)
            v_image = vehicle_information.vehicle_image()
            return v_image

        else:
            # -> Request was not successful
            ErrorContent = 'Status Code: {}, Reason: {}'.format(r.status_code, r.reason)
            return ErrorContent

    def check_response(self, r, agent_price):
        """
            @params
                r - To pass in a request object for the UKVD API 
                    Data Package.
                agent_price - To pass in the agents offered price
                              per kg.

            @returns
                valuation_data - returns a dictionary with the 
                                 valuation information.
                ErrorContent - returns the error of the failed 
                               request.
        """
        # Check for a successful response
        if r.status_code == requests.codes.ok:
            # -> Request was successful

            # Get function (get_vehicle_information()).
            get_vehicle_info = GetVehicleInformation(r)
            vehicle_details = get_vehicle_info.vehicle_details()
            # price offered intiializer.
            price_offered = 0.0
            try:
                # Get vehicle kerb weight.
                vehicle_kw = vehicle_details["vehicle_kw"]
                # Get price per kg against vehicle kerb weight.
                price_offered = vehicle_kw_calculation(vehicle_kw, agent_price)
            except KeyError:
                pass

            # Public vehicle valuation data.
            valuation_data = {
                "vehicle_information": vehicle_details,
                "price_offered": price_offered
            }
            return valuation_data
        
        else:
            # -> Request was not successful
            ErrorContent = 'Status Code: {}, Reason: {}'.format(r.status_code, r.reason)
            # For Debugging purposes only
            # and should be removed before production.
            print("\n\n\nUKVD Error: {0}\n\n\n\n".format(str(ErrorContent)))
            return ErrorContent
