# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = add_to_cart_from_dict(json.loads(json_string))
#     result = add_to_list_from_dict(json.loads(json_string))
#     result = api_settings_from_dict(json.loads(json_string))
#     result = category_page_view_from_dict(json.loads(json_string))
#     result = change_item_stock_state_from_dict(json.loads(json_string))
#     result = checkout_start_from_dict(json.loads(json_string))
#     result = common_from_dict(json.loads(json_string))
#     result = detail_product_view_from_dict(json.loads(json_string))
#     result = home_page_view_from_dict(json.loads(json_string))
#     result = image_interaction_from_dict(json.loads(json_string))
#     result = remove_item_from_dict(json.loads(json_string))
#     result = upsert_item_from_dict(json.loads(json_string))
#     result = list_view_from_dict(json.loads(json_string))
#     result = offline_recommendations_remove_from_dict(json.loads(json_string))
#     result = offline_recommendations_upsert_from_dict(json.loads(json_string))
#     result = other_interaction_from_dict(json.loads(json_string))
#     result = page_visit_from_dict(json.loads(json_string))
#     result = placement_remove_from_dict(json.loads(json_string))
#     result = placement_upsert_from_dict(json.loads(json_string))
#     result = purchase_complete_from_dict(json.loads(json_string))
#     result = rate_product_from_dict(json.loads(json_string))
#     result = reco_request_from_dict(json.loads(json_string))
#     result = reco_show_from_dict(json.loads(json_string))
#     result = remove_from_cart_from_dict(json.loads(json_string))
#     result = remove_from_list_from_dict(json.loads(json_string))
#     result = search_items_from_dict(json.loads(json_string))
#     result = cart_page_view_from_dict(json.loads(json_string))
#     result = smart_search_request_from_dict(json.loads(json_string))
#     result = smart_search_show_from_dict(json.loads(json_string))
#     result = sort_items_from_dict(json.loads(json_string))
#     result = unknown_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Union, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class EventDetail:
    rec_id: str
    url: str
    event_attributes: Optional[Dict[str, str]] = None
    experiment_ids: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EventDetail':
        assert isinstance(obj, dict)
        rec_id = from_str(obj.get("rec_id"))
        url = from_str(obj.get("url"))
        event_attributes = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("event_attributes"))
        experiment_ids = from_union([from_none, from_int], obj.get("experiment_ids"))
        return EventDetail(rec_id, url, event_attributes, experiment_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rec_id"] = from_str(self.rec_id)
        result["url"] = from_str(self.url)
        result["event_attributes"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.event_attributes)
        result["experiment_ids"] = from_union([from_none, from_int], self.experiment_ids)
        return result


class EventType(Enum):
    ADD_TO_CART = "AddToCart"
    ADD_TO_LIST = "AddToList"
    CART_PAGE_VIEW = "CartPageView"
    CATEGORY_PAGE_VIEW = "CategoryPageView"
    CHANGE_ITEM_STOCK_STATE = "ChangeItemStockState"
    CHECKOUT_START = "CheckoutStart"
    DETAIL_PRODUCT_VIEW = "DetailProductView"
    HOME_PAGE_VIEW = "HomePageView"
    IMAGE_INTERACTION = "ImageInteraction"
    ITEM_REMOVE = "ItemRemove"
    ITEM_UPSERT = "ItemUpsert"
    LIST_VIEW = "ListView"
    OFFLINE_RECOMMENDATIONS_REMOVE = "OfflineRecommendationsRemove"
    OFFLINE_RECOMMENDATIONS_UPSERT = "OfflineRecommendationsUpsert"
    OTHER_INTERACTION = "OtherInteraction"
    PAGE_VISIT = "PageVisit"
    PLACEMENT_REMOVE = "PlacementRemove"
    PLACEMENT_UPSERT = "PlacementUpsert"
    PURCHASE_COMPLETE = "PurchaseComplete"
    RATE_PRODUCT = "RateProduct"
    RECO_REQUEST = "RecoRequest"
    RECO_SHOW = "RecoShow"
    REMOVE_FROM_CART = "RemoveFromCart"
    REMOVE_FROM_LIST = "RemoveFromList"
    SEARCH_ITEMS = "SearchItems"
    SMART_SEARCH_REQUEST = "SmartSearchRequest"
    SMART_SEARCH_SHOW = "SmartSearchShow"
    SORT_ITEMS = "SortItems"
    UNKNOWN_EVENT = "UnknownEvent"


class Currency(Enum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYN = "BYN"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRU = "MRU"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STN = "STN"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    UNK = "UNK"
    USD = "USD"
    USN = "USN"
    UYI = "UYI"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPF = "XPF"
    XSU = "XSU"
    XUA = "XUA"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWL = "ZWL"


@dataclass
class ItemDetails:
    item_id: str
    currency_code: Optional[Currency] = None
    display_price: Optional[float] = None
    original_price: Optional[float] = None
    quantity: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemDetails':
        assert isinstance(obj, dict)
        item_id = from_str(obj.get("item_id"))
        currency_code = from_union([from_none, Currency], obj.get("currency_code"))
        display_price = from_union([from_none, from_float], obj.get("display_price"))
        original_price = from_union([from_none, from_float], obj.get("original_price"))
        quantity = from_union([from_none, from_int], obj.get("quantity"))
        return ItemDetails(item_id, currency_code, display_price, original_price, quantity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["item_id"] = from_str(self.item_id)
        result["currency_code"] = from_union([from_none, lambda x: to_enum(Currency, x)], self.currency_code)
        result["display_price"] = from_union([from_none, to_float], self.display_price)
        result["original_price"] = from_union([from_none, to_float], self.original_price)
        result["quantity"] = from_union([from_none, from_int], self.quantity)
        return result


class Gender(Enum):
    FEMALE = "Female"
    MALE = "Male"
    OTHER = "Other"


@dataclass
class UserAdditionalInfo:
    birth_year: Optional[int] = None
    gender: Optional[Gender] = None
    ip: Optional[str] = None
    location: Optional[str] = None
    session_id: Optional[str] = None
    user_agent: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserAdditionalInfo':
        assert isinstance(obj, dict)
        birth_year = from_union([from_none, from_int], obj.get("birth_year"))
        gender = from_union([from_none, Gender], obj.get("gender"))
        ip = from_union([from_none, from_str], obj.get("ip"))
        location = from_union([from_none, from_str], obj.get("location"))
        session_id = from_union([from_none, from_str], obj.get("session_id"))
        user_agent = from_union([from_none, from_str], obj.get("user_agent"))
        return UserAdditionalInfo(birth_year, gender, ip, location, session_id, user_agent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["birth_year"] = from_union([from_none, from_int], self.birth_year)
        result["gender"] = from_union([from_none, lambda x: to_enum(Gender, x)], self.gender)
        result["ip"] = from_union([from_none, from_str], self.ip)
        result["location"] = from_union([from_none, from_str], self.location)
        result["session_id"] = from_union([from_none, from_str], self.session_id)
        result["user_agent"] = from_union([from_none, from_str], self.user_agent)
        return result


@dataclass
class UserInfo:
    visitor_id: str
    additional_info: Optional[UserAdditionalInfo] = None
    session_id: Optional[str] = None
    user_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserInfo':
        assert isinstance(obj, dict)
        visitor_id = from_str(obj.get("visitor_id"))
        additional_info = from_union([UserAdditionalInfo.from_dict, from_none], obj.get("additional_info"))
        session_id = from_union([from_none, from_str], obj.get("session_id"))
        user_id = from_union([from_none, from_str], obj.get("user_id"))
        return UserInfo(visitor_id, additional_info, session_id, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["visitor_id"] = from_str(self.visitor_id)
        result["additional_info"] = from_union([lambda x: to_class(UserAdditionalInfo, x), from_none], self.additional_info)
        result["session_id"] = from_union([from_none, from_str], self.session_id)
        result["user_id"] = from_union([from_none, from_str], self.user_id)
        return result


@dataclass
class AddToCart:
    event_type: EventType
    item: ItemDetails
    user_info: UserInfo
    cart_id: Optional[str] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AddToCart':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        cart_id = from_union([from_none, from_str], obj.get("cart_id"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return AddToCart(event_type, item, user_info, cart_id, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(ItemDetails, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["cart_id"] = from_union([from_none, from_str], self.cart_id)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class AddToList:
    event_type: EventType
    item: ItemDetails
    list_id: str
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AddToList':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        list_id = from_str(obj.get("list_id"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return AddToList(event_type, item, list_id, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(ItemDetails, self.item)
        result["list_id"] = from_str(self.list_id)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class APISettings:
    url_api: str

    @staticmethod
    def from_dict(obj: Any) -> 'APISettings':
        assert isinstance(obj, dict)
        url_api = from_str(obj.get("url_api"))
        return APISettings(url_api)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url_api"] = from_str(self.url_api)
        return result


@dataclass
class CategoryPageView:
    event_type: EventType
    items: List[ItemDetails]
    on_screen: bool
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    page_categories: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CategoryPageView':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        on_screen = from_bool(obj.get("on_screen"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        page_categories = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("page_categories"))
        return CategoryPageView(event_type, items, on_screen, user_info, event_detail, event_time, page_categories)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["on_screen"] = from_bool(self.on_screen)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["page_categories"] = from_union([from_none, lambda x: from_list(from_str, x)], self.page_categories)
        return result


class StockState(Enum):
    BACK_ORDER = "BackOrder"
    IN_STOCK = "InStock"
    OUT_OF_STOCK = "OutOfStock"
    PRE_ORDER = "PreOrder"


@dataclass
class ChangeItemStockState:
    event_type: EventType
    item_id: str
    stock_state: StockState
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChangeItemStockState':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item_id = from_str(obj.get("item_id"))
        stock_state = StockState(obj.get("stock_state"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return ChangeItemStockState(event_type, item_id, stock_state, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item_id"] = from_str(self.item_id)
        result["stock_state"] = to_enum(StockState, self.stock_state)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class Costs:
    cost: Optional[float] = None
    manufacturing: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Costs':
        assert isinstance(obj, dict)
        cost = from_union([from_none, from_float], obj.get("cost"))
        manufacturing = from_union([from_none, from_float], obj.get("manufacturing"))
        return Costs(cost, manufacturing)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cost"] = from_union([from_none, to_float], self.cost)
        result["manufacturing"] = from_union([from_none, to_float], self.manufacturing)
        return result


@dataclass
class Taxes:
    local: Optional[float] = None
    state: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Taxes':
        assert isinstance(obj, dict)
        local = from_union([from_none, from_float], obj.get("local"))
        state = from_union([from_none, from_float], obj.get("state"))
        return Taxes(local, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["local"] = from_union([from_none, to_float], self.local)
        result["state"] = from_union([from_none, to_float], self.state)
        return result


@dataclass
class PurchaseTransaction:
    currency_code: Currency
    revenue: float
    costs: Optional[Costs] = None
    id: Optional[str] = None
    taxes: Optional[Taxes] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurchaseTransaction':
        assert isinstance(obj, dict)
        currency_code = Currency(obj.get("currency_code"))
        revenue = from_float(obj.get("revenue"))
        costs = from_union([Costs.from_dict, from_none], obj.get("costs"))
        id = from_union([from_none, from_str], obj.get("id"))
        taxes = from_union([Taxes.from_dict, from_none], obj.get("taxes"))
        return PurchaseTransaction(currency_code, revenue, costs, id, taxes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["currency_code"] = to_enum(Currency, self.currency_code)
        result["revenue"] = to_float(self.revenue)
        result["costs"] = from_union([lambda x: to_class(Costs, x), from_none], self.costs)
        result["id"] = from_union([from_none, from_str], self.id)
        result["taxes"] = from_union([lambda x: to_class(Taxes, x), from_none], self.taxes)
        return result


@dataclass
class CheckoutStart:
    event_type: EventType
    items: List[ItemDetails]
    purchase_transaction: PurchaseTransaction
    user_info: UserInfo
    cart_id: Optional[str] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CheckoutStart':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        purchase_transaction = PurchaseTransaction.from_dict(obj.get("purchase_transaction"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        cart_id = from_union([from_none, from_str], obj.get("cart_id"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return CheckoutStart(event_type, items, purchase_transaction, user_info, cart_id, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["purchase_transaction"] = to_class(PurchaseTransaction, self.purchase_transaction)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["cart_id"] = from_union([from_none, from_str], self.cart_id)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class DetailProductView:
    event_type: EventType
    item: ItemDetails
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    rec_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DetailProductView':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        rec_id = from_union([from_none, from_str], obj.get("rec_id"))
        return DetailProductView(event_type, item, user_info, event_detail, event_time, rec_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(ItemDetails, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["rec_id"] = from_union([from_none, from_str], self.rec_id)
        return result


@dataclass
class HomePageView:
    event_type: EventType
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'HomePageView':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return HomePageView(event_type, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class ImageInteraction:
    event_type: EventType
    item: ItemDetails
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageInteraction':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return ImageInteraction(event_type, item, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(ItemDetails, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class RemoveItem:
    event_time: int
    event_type: EventType
    item_id: str
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoveItem':
        assert isinstance(obj, dict)
        event_time = from_int(obj.get("event_time"))
        event_type = EventType(obj.get("event_type"))
        item_id = from_str(obj.get("item_id"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        return RemoveItem(event_time, event_type, item_id, user_info, event_detail)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_time"] = from_int(self.event_time)
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item_id"] = from_str(self.item_id)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        return result


@dataclass
class Image:
    height: str
    uri: str
    width: str

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        height = from_str(obj.get("height"))
        uri = from_str(obj.get("uri"))
        width = from_str(obj.get("width"))
        return Image(height, uri, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["height"] = from_str(self.height)
        result["uri"] = from_str(self.uri)
        result["width"] = from_str(self.width)
        return result


@dataclass
class ExactPrice:
    display_price: float
    original_price: float

    @staticmethod
    def from_dict(obj: Any) -> 'ExactPrice':
        assert isinstance(obj, dict)
        display_price = from_float(obj.get("display_price"))
        original_price = from_float(obj.get("original_price"))
        return ExactPrice(display_price, original_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["display_price"] = to_float(self.display_price)
        result["original_price"] = to_float(self.original_price)
        return result


@dataclass
class ProductDetails:
    currency_code: Currency
    id: str
    price: ExactPrice
    stock_state: StockState
    title: str
    attributes: Optional[Dict[str, str]] = None
    available_quantity: Optional[int] = None
    canonical_product_uri: Optional[str] = None
    categorical_attributes: Optional[Dict[str, str]] = None
    categories: Optional[List[List[str]]] = None
    costs: Optional[Dict[str, float]] = None
    description: Optional[str] = None
    images: Optional[List[Image]] = None
    item_group_id: Optional[str] = None
    language_code: Optional[str] = None
    numeric_attributes: Optional[Dict[str, float]] = None
    product_code: Optional[str] = None
    tags: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProductDetails':
        assert isinstance(obj, dict)
        currency_code = Currency(obj.get("currency_code"))
        id = from_str(obj.get("id"))
        price = ExactPrice.from_dict(obj.get("price"))
        stock_state = StockState(obj.get("stock_state"))
        title = from_str(obj.get("title"))
        attributes = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("attributes"))
        available_quantity = from_union([from_none, from_int], obj.get("available_quantity"))
        canonical_product_uri = from_union([from_none, from_str], obj.get("canonical_product_uri"))
        categorical_attributes = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("categorical_attributes"))
        categories = from_union([from_none, lambda x: from_list(lambda x: from_list(from_str, x), x)], obj.get("categories"))
        costs = from_union([from_none, lambda x: from_dict(from_float, x)], obj.get("costs"))
        description = from_union([from_none, from_str], obj.get("description"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        item_group_id = from_union([from_none, from_str], obj.get("item_group_id"))
        language_code = from_union([from_none, from_str], obj.get("language_code"))
        numeric_attributes = from_union([from_none, lambda x: from_dict(from_float, x)], obj.get("numeric_attributes"))
        product_code = from_union([from_none, from_str], obj.get("product_code"))
        tags = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("tags"))
        return ProductDetails(currency_code, id, price, stock_state, title, attributes, available_quantity, canonical_product_uri, categorical_attributes, categories, costs, description, images, item_group_id, language_code, numeric_attributes, product_code, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["currency_code"] = to_enum(Currency, self.currency_code)
        result["id"] = from_str(self.id)
        result["price"] = to_class(ExactPrice, self.price)
        result["stock_state"] = to_enum(StockState, self.stock_state)
        result["title"] = from_str(self.title)
        result["attributes"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.attributes)
        result["available_quantity"] = from_union([from_none, from_int], self.available_quantity)
        result["canonical_product_uri"] = from_union([from_none, from_str], self.canonical_product_uri)
        result["categorical_attributes"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.categorical_attributes)
        result["categories"] = from_union([from_none, lambda x: from_list(lambda x: from_list(from_str, x), x)], self.categories)
        result["costs"] = from_union([from_none, lambda x: from_dict(to_float, x)], self.costs)
        result["description"] = from_union([from_none, from_str], self.description)
        result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        result["item_group_id"] = from_union([from_none, from_str], self.item_group_id)
        result["language_code"] = from_union([from_none, from_str], self.language_code)
        result["numeric_attributes"] = from_union([from_none, lambda x: from_dict(to_float, x)], self.numeric_attributes)
        result["product_code"] = from_union([from_none, from_str], self.product_code)
        result["tags"] = from_union([from_none, lambda x: from_list(from_str, x)], self.tags)
        return result


@dataclass
class UpsertItem:
    event_time: int
    event_type: EventType
    product_details: ProductDetails
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UpsertItem':
        assert isinstance(obj, dict)
        event_time = from_int(obj.get("event_time"))
        event_type = EventType(obj.get("event_type"))
        product_details = ProductDetails.from_dict(obj.get("product_details"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        return UpsertItem(event_time, event_type, product_details, user_info, event_detail)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_time"] = from_int(self.event_time)
        result["event_type"] = to_enum(EventType, self.event_type)
        result["product_details"] = to_class(ProductDetails, self.product_details)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        return result


@dataclass
class ListView:
    event_type: EventType
    items: List[ItemDetails]
    list_id: str
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListView':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        list_id = from_str(obj.get("list_id"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return ListView(event_type, items, list_id, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["list_id"] = from_str(self.list_id)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class OfflineRecommendationsTypeClass:
    other_similarity: str

    @staticmethod
    def from_dict(obj: Any) -> 'OfflineRecommendationsTypeClass':
        assert isinstance(obj, dict)
        other_similarity = from_str(obj.get("OtherSimilarity"))
        return OfflineRecommendationsTypeClass(other_similarity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["OtherSimilarity"] = from_str(self.other_similarity)
        return result


class OfflineRecommendationsTypeEnum(Enum):
    IMAGE_SIMILARITY = "ImageSimilarity"
    TEXT_SIMILARITY = "TextSimilarity"


@dataclass
class OfflineRecommendationsRemove:
    event_type: EventType
    name: Union[OfflineRecommendationsTypeClass, OfflineRecommendationsTypeEnum]
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OfflineRecommendationsRemove':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        name = from_union([OfflineRecommendationsTypeClass.from_dict, OfflineRecommendationsTypeEnum], obj.get("name"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return OfflineRecommendationsRemove(event_type, name, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["name"] = from_union([lambda x: to_class(OfflineRecommendationsTypeClass, x), lambda x: to_enum(OfflineRecommendationsTypeEnum, x)], self.name)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class OfflineRecommendationsUpsert:
    event_type: EventType
    matrix: Dict[str, Dict[str, int]]
    name: Union[OfflineRecommendationsTypeClass, OfflineRecommendationsTypeEnum]
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OfflineRecommendationsUpsert':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        matrix = from_dict(lambda x: from_dict(from_int, x), obj.get("matrix"))
        name = from_union([OfflineRecommendationsTypeClass.from_dict, OfflineRecommendationsTypeEnum], obj.get("name"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return OfflineRecommendationsUpsert(event_type, matrix, name, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["matrix"] = from_dict(lambda x: from_dict(from_int, x), self.matrix)
        result["name"] = from_union([lambda x: to_class(OfflineRecommendationsTypeClass, x), lambda x: to_enum(OfflineRecommendationsTypeEnum, x)], self.name)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class OtherInteraction:
    event_type: EventType
    interaction_name: str
    item: ItemDetails
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OtherInteraction':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        interaction_name = from_str(obj.get("interaction_name"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return OtherInteraction(event_type, interaction_name, item, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["interaction_name"] = from_str(self.interaction_name)
        result["item"] = to_class(ItemDetails, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class PageVisit:
    event_type: EventType
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PageVisit':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return PageVisit(event_type, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class PlacementRemove:
    event_type: EventType
    name: str
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlacementRemove':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        name = from_str(obj.get("name"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return PlacementRemove(event_type, name, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["name"] = from_str(self.name)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


class RankingStrategy(Enum):
    DIRICHLET_SAMPLING = "DirichletSampling"
    RANKING_MODEL = "RankingModel"
    THOMSPON_SAMPLING = "ThomsponSampling"
    WEIGHTED_SAMPLE = "WeightedSample"


@dataclass
class GenericStrategyClass:
    similar_offline: Optional[str] = None
    query: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GenericStrategyClass':
        assert isinstance(obj, dict)
        similar_offline = from_union([from_str, from_none], obj.get("SimilarOffline"))
        query = from_union([from_str, from_none], obj.get("Query"))
        return GenericStrategyClass(similar_offline, query)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SimilarOffline"] = from_union([from_str, from_none], self.similar_offline)
        result["Query"] = from_union([from_str, from_none], self.query)
        return result


class GenericStrategyEnum(Enum):
    ALSO_ADDED_TO_CART = "AlsoAddedToCart"
    ALSO_PURCHASED = "AlsoPurchased"
    ALSO_SEEN = "AlsoSeen"
    BESTSELLER_CATEGORY = "BestsellerCategory"
    BESTSELLER_GLOBAL = "BestsellerGlobal"
    CONTENT_MATCHING = "ContentMatching"
    MOST_PURCHASES = "MostPurchases"
    MOST_VIEWS = "MostViews"
    SEARCH_MATCHING = "SearchMatching"
    SEEN_IN_SESSION = "SeenInSession"
    SEEN_IN_SESSION_COCCUR_ADDED_TO_CART = "SeenInSessionCoccurAddedToCart"
    SEEN_IN_SESSION_COCCUR_SEEN = "SeenInSessionCoccurSeen"
    SIMILAR_ATTRIBUTES = "SimilarAttributes"
    SIMILAR_IMAGE = "SimilarImage"
    SIMILAR_TEXT = "SimilarText"


@dataclass
class WeightedGenericCandidateRec:
    strategy: Union[GenericStrategyClass, GenericStrategyEnum]
    weight: float

    @staticmethod
    def from_dict(obj: Any) -> 'WeightedGenericCandidateRec':
        assert isinstance(obj, dict)
        strategy = from_union([GenericStrategyClass.from_dict, GenericStrategyEnum], obj.get("strategy"))
        weight = from_float(obj.get("weight"))
        return WeightedGenericCandidateRec(strategy, weight)

    def to_dict(self) -> dict:
        result: dict = {}
        result["strategy"] = from_union([lambda x: to_class(GenericStrategyClass, x), lambda x: to_enum(GenericStrategyEnum, x)], self.strategy)
        result["weight"] = to_float(self.weight)
        return result


@dataclass
class PlacementUpsert:
    event_type: EventType
    name: str
    ranking: RankingStrategy
    strategies: List[WeightedGenericCandidateRec]
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    url_params: Optional[Dict[str, str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlacementUpsert':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        name = from_str(obj.get("name"))
        ranking = RankingStrategy(obj.get("ranking"))
        strategies = from_list(WeightedGenericCandidateRec.from_dict, obj.get("strategies"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        url_params = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("url_params"))
        return PlacementUpsert(event_type, name, ranking, strategies, user_info, event_detail, event_time, url_params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["name"] = from_str(self.name)
        result["ranking"] = to_enum(RankingStrategy, self.ranking)
        result["strategies"] = from_list(lambda x: to_class(WeightedGenericCandidateRec, x), self.strategies)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["url_params"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.url_params)
        return result


@dataclass
class PurchaseComplete:
    event_type: EventType
    items: List[ItemDetails]
    purchase_transaction: PurchaseTransaction
    user_info: UserInfo
    cart_id: Optional[str] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurchaseComplete':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        purchase_transaction = PurchaseTransaction.from_dict(obj.get("purchase_transaction"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        cart_id = from_union([from_none, from_str], obj.get("cart_id"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return PurchaseComplete(event_type, items, purchase_transaction, user_info, cart_id, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["purchase_transaction"] = to_class(PurchaseTransaction, self.purchase_transaction)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["cart_id"] = from_union([from_none, from_str], self.cart_id)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class RateProduct:
    event_type: EventType
    item: ItemDetails
    user_info: UserInfo
    comment: Optional[str] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    rating: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RateProduct':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        comment = from_union([from_none, from_str], obj.get("comment"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        rating = from_union([from_none, from_float], obj.get("rating"))
        return RateProduct(event_type, item, user_info, comment, event_detail, event_time, rating)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(ItemDetails, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["comment"] = from_union([from_none, from_str], self.comment)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["rating"] = from_union([from_none, to_float], self.rating)
        return result


@dataclass
class PageInfo:
    content: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PageInfo':
        assert isinstance(obj, dict)
        content = from_union([from_none, from_str], obj.get("content"))
        url = from_union([from_none, from_str], obj.get("url"))
        return PageInfo(content, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content"] = from_union([from_none, from_str], self.content)
        result["url"] = from_union([from_none, from_str], self.url)
        return result


@dataclass
class SearchInfo:
    query: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SearchInfo':
        assert isinstance(obj, dict)
        query = from_union([from_none, from_str], obj.get("query"))
        return SearchInfo(query)

    def to_dict(self) -> dict:
        result: dict = {}
        result["query"] = from_union([from_none, from_str], self.query)
        return result


@dataclass
class LocationClass:
    product_page: Optional[str] = None
    add_to_cart: Optional[str] = None
    category_page: Optional[List[str]] = None
    search_page: Optional[SearchInfo] = None
    checkout_page: Optional[List[str]] = None
    other_page: Optional[PageInfo] = None
    unknown_page: Optional[PageInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LocationClass':
        assert isinstance(obj, dict)
        product_page = from_union([from_str, from_none], obj.get("ProductPage"))
        add_to_cart = from_union([from_str, from_none], obj.get("AddToCart"))
        category_page = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("CategoryPage"))
        search_page = from_union([SearchInfo.from_dict, from_none], obj.get("SearchPage"))
        checkout_page = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("CheckoutPage"))
        other_page = from_union([PageInfo.from_dict, from_none], obj.get("OtherPage"))
        unknown_page = from_union([PageInfo.from_dict, from_none], obj.get("UnknownPage"))
        return LocationClass(product_page, add_to_cart, category_page, search_page, checkout_page, other_page, unknown_page)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ProductPage"] = from_union([from_str, from_none], self.product_page)
        result["AddToCart"] = from_union([from_str, from_none], self.add_to_cart)
        result["CategoryPage"] = from_union([from_none, lambda x: from_list(from_str, x)], self.category_page)
        result["SearchPage"] = from_union([lambda x: to_class(SearchInfo, x), from_none], self.search_page)
        result["CheckoutPage"] = from_union([from_none, lambda x: from_list(from_str, x)], self.checkout_page)
        result["OtherPage"] = from_union([lambda x: to_class(PageInfo, x), from_none], self.other_page)
        result["UnknownPage"] = from_union([lambda x: to_class(PageInfo, x), from_none], self.unknown_page)
        return result


class LocationEnum(Enum):
    ERROR404 = "Error404"
    HOME_PAGE = "HomePage"


@dataclass
class RecoRequest:
    event_type: EventType
    location: Union[LocationClass, LocationEnum]
    n_items: int
    user_info: UserInfo
    additional_uri_params: Optional[Dict[str, str]] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    placement_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecoRequest':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        location = from_union([LocationClass.from_dict, LocationEnum], obj.get("location"))
        n_items = from_int(obj.get("n_items"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        additional_uri_params = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("additional_uri_params"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        placement_name = from_union([from_none, from_str], obj.get("placement_name"))
        return RecoRequest(event_type, location, n_items, user_info, additional_uri_params, event_detail, event_time, placement_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["location"] = from_union([lambda x: to_class(LocationClass, x), lambda x: to_enum(LocationEnum, x)], self.location)
        result["n_items"] = from_int(self.n_items)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["additional_uri_params"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.additional_uri_params)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["placement_name"] = from_union([from_none, from_str], self.placement_name)
        return result


@dataclass
class ProductDetailsRecoShow:
    currency_code: Currency
    id: str
    price: ExactPrice
    product_code: str
    rec_id: str
    title: str
    canonical_product_uri: Optional[str] = None
    canonical_product_uri_with_params: Optional[str] = None
    categories: Optional[List[List[str]]] = None
    images: Optional[List[Image]] = None
    score: Optional[float] = None
    strategies_used: Optional[Dict[str, float]] = None
    url_params: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProductDetailsRecoShow':
        assert isinstance(obj, dict)
        currency_code = Currency(obj.get("currency_code"))
        id = from_str(obj.get("id"))
        price = ExactPrice.from_dict(obj.get("price"))
        product_code = from_str(obj.get("product_code"))
        rec_id = from_str(obj.get("rec_id"))
        title = from_str(obj.get("title"))
        canonical_product_uri = from_union([from_none, from_str], obj.get("canonical_product_uri"))
        canonical_product_uri_with_params = from_union([from_none, from_str], obj.get("canonical_product_uri_with_params"))
        categories = from_union([from_none, lambda x: from_list(lambda x: from_list(from_str, x), x)], obj.get("categories"))
        images = from_union([from_none, lambda x: from_list(Image.from_dict, x)], obj.get("images"))
        score = from_union([from_none, from_float], obj.get("score"))
        strategies_used = from_union([from_none, lambda x: from_dict(from_float, x)], obj.get("strategies_used"))
        url_params = from_union([from_none, from_str], obj.get("url_params"))
        return ProductDetailsRecoShow(currency_code, id, price, product_code, rec_id, title, canonical_product_uri, canonical_product_uri_with_params, categories, images, score, strategies_used, url_params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["currency_code"] = to_enum(Currency, self.currency_code)
        result["id"] = from_str(self.id)
        result["price"] = to_class(ExactPrice, self.price)
        result["product_code"] = from_str(self.product_code)
        result["rec_id"] = from_str(self.rec_id)
        result["title"] = from_str(self.title)
        result["canonical_product_uri"] = from_union([from_none, from_str], self.canonical_product_uri)
        result["canonical_product_uri_with_params"] = from_union([from_none, from_str], self.canonical_product_uri_with_params)
        result["categories"] = from_union([from_none, lambda x: from_list(lambda x: from_list(from_str, x), x)], self.categories)
        result["images"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Image, x), x)], self.images)
        result["score"] = from_union([from_none, to_float], self.score)
        result["strategies_used"] = from_union([from_none, lambda x: from_dict(to_float, x)], self.strategies_used)
        result["url_params"] = from_union([from_none, from_str], self.url_params)
        return result


@dataclass
class RecoShow:
    event_type: EventType
    items: List[ProductDetailsRecoShow]
    location: Union[LocationClass, LocationEnum]
    user_info: UserInfo
    additional_uri_params: Optional[Dict[str, str]] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    experiment_id: Optional[str] = None
    placement_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecoShow':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ProductDetailsRecoShow.from_dict, obj.get("items"))
        location = from_union([LocationClass.from_dict, LocationEnum], obj.get("location"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        additional_uri_params = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("additional_uri_params"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        experiment_id = from_union([from_none, from_str], obj.get("experiment_id"))
        placement_name = from_union([from_none, from_str], obj.get("placement_name"))
        return RecoShow(event_type, items, location, user_info, additional_uri_params, event_detail, event_time, experiment_id, placement_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ProductDetailsRecoShow, x), self.items)
        result["location"] = from_union([lambda x: to_class(LocationClass, x), lambda x: to_enum(LocationEnum, x)], self.location)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["additional_uri_params"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.additional_uri_params)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["experiment_id"] = from_union([from_none, from_str], self.experiment_id)
        result["placement_name"] = from_union([from_none, from_str], self.placement_name)
        return result


@dataclass
class RemoveFromCart:
    event_type: EventType
    item: ItemDetails
    user_info: UserInfo
    cart_id: Optional[str] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoveFromCart':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        cart_id = from_union([from_none, from_str], obj.get("cart_id"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return RemoveFromCart(event_type, item, user_info, cart_id, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(ItemDetails, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["cart_id"] = from_union([from_none, from_str], self.cart_id)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class RemoveFromList:
    event_type: EventType
    items: List[ItemDetails]
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    list_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoveFromList':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        list_id = from_union([from_none, from_str], obj.get("list_id"))
        return RemoveFromList(event_type, items, user_info, event_detail, event_time, list_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["list_id"] = from_union([from_none, from_str], self.list_id)
        return result


@dataclass
class SearchItems:
    event_type: EventType
    items: List[ItemDetails]
    query: str
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SearchItems':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        query = from_str(obj.get("query"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return SearchItems(event_type, items, query, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["query"] = from_str(self.query)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class CartPageView:
    event_type: EventType
    items: List[ItemDetails]
    user_info: UserInfo
    cart_id: Optional[str] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CartPageView':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        cart_id = from_union([from_none, from_str], obj.get("cart_id"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return CartPageView(event_type, items, user_info, cart_id, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["cart_id"] = from_union([from_none, from_str], self.cart_id)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


class SearchOrder(Enum):
    NEWEST = "Newest"
    OLDEST = "Oldest"
    PERSONALIZED = "Personalized"
    POPULARITY_ASC = "PopularityAsc"
    POPULARITY_DESC = "PopularityDesc"
    PRICE_ASC = "PriceAsc"
    PRICE_DESC = "PriceDesc"
    RATING_ASC = "RatingAsc"
    RATING_DESC = "RatingDesc"
    RELEVANCE_ASC = "RelevanceAsc"
    RELEVANCE_DESC = "RelevanceDesc"


@dataclass
class SmartSearchRequest:
    event_type: EventType
    filter: Dict[str, str]
    n_items: int
    page: int
    query: str
    search_order: SearchOrder
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SmartSearchRequest':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        filter = from_dict(from_str, obj.get("filter"))
        n_items = from_int(obj.get("n_items"))
        page = from_int(obj.get("page"))
        query = from_str(obj.get("query"))
        search_order = SearchOrder(obj.get("search_order"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return SmartSearchRequest(event_type, filter, n_items, page, query, search_order, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["filter"] = from_dict(from_str, self.filter)
        result["n_items"] = from_int(self.n_items)
        result["page"] = from_int(self.page)
        result["query"] = from_str(self.query)
        result["search_order"] = to_enum(SearchOrder, self.search_order)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class SmartSearchShow:
    event_type: EventType
    items: List[ProductDetailsRecoShow]
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SmartSearchShow':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ProductDetailsRecoShow.from_dict, obj.get("items"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return SmartSearchShow(event_type, items, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ProductDetailsRecoShow, x), self.items)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


class SortOrder(Enum):
    NAME_ASC = "NameAsc"
    NAME_DESC = "NameDesc"
    POPULARITY_ASC = "PopularityAsc"
    POPULARITY_DESC = "PopularityDesc"
    PRICE_ASC = "PriceAsc"
    PRICE_DESC = "PriceDesc"
    RATING_ASC = "RatingAsc"
    RATING_DESC = "RatingDesc"


@dataclass
class SortItems:
    event_type: EventType
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    sort_order: Optional[SortOrder] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SortItems':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        sort_order = from_union([from_none, SortOrder], obj.get("sort_order"))
        return SortItems(event_type, user_info, event_detail, event_time, sort_order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["sort_order"] = from_union([from_none, lambda x: to_enum(SortOrder, x)], self.sort_order)
        return result


@dataclass
class UnknownEvent:
    event_type: EventType
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UnknownEvent':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return UnknownEvent(event_type, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


def add_to_cart_from_dict(s: Any) -> AddToCart:
    return AddToCart.from_dict(s)


def add_to_cart_to_dict(x: AddToCart) -> Any:
    return to_class(AddToCart, x)


def add_to_list_from_dict(s: Any) -> AddToList:
    return AddToList.from_dict(s)


def add_to_list_to_dict(x: AddToList) -> Any:
    return to_class(AddToList, x)


def api_settings_from_dict(s: Any) -> APISettings:
    return APISettings.from_dict(s)


def api_settings_to_dict(x: APISettings) -> Any:
    return to_class(APISettings, x)


def category_page_view_from_dict(s: Any) -> CategoryPageView:
    return CategoryPageView.from_dict(s)


def category_page_view_to_dict(x: CategoryPageView) -> Any:
    return to_class(CategoryPageView, x)


def change_item_stock_state_from_dict(s: Any) -> ChangeItemStockState:
    return ChangeItemStockState.from_dict(s)


def change_item_stock_state_to_dict(x: ChangeItemStockState) -> Any:
    return to_class(ChangeItemStockState, x)


def checkout_start_from_dict(s: Any) -> CheckoutStart:
    return CheckoutStart.from_dict(s)


def checkout_start_to_dict(x: CheckoutStart) -> Any:
    return to_class(CheckoutStart, x)


def common_from_dict(s: Any) -> Any:
    return s


def common_to_dict(x: Any) -> Any:
    return x


def detail_product_view_from_dict(s: Any) -> DetailProductView:
    return DetailProductView.from_dict(s)


def detail_product_view_to_dict(x: DetailProductView) -> Any:
    return to_class(DetailProductView, x)


def home_page_view_from_dict(s: Any) -> HomePageView:
    return HomePageView.from_dict(s)


def home_page_view_to_dict(x: HomePageView) -> Any:
    return to_class(HomePageView, x)


def image_interaction_from_dict(s: Any) -> ImageInteraction:
    return ImageInteraction.from_dict(s)


def image_interaction_to_dict(x: ImageInteraction) -> Any:
    return to_class(ImageInteraction, x)


def remove_item_from_dict(s: Any) -> RemoveItem:
    return RemoveItem.from_dict(s)


def remove_item_to_dict(x: RemoveItem) -> Any:
    return to_class(RemoveItem, x)


def upsert_item_from_dict(s: Any) -> UpsertItem:
    return UpsertItem.from_dict(s)


def upsert_item_to_dict(x: UpsertItem) -> Any:
    return to_class(UpsertItem, x)


def list_view_from_dict(s: Any) -> ListView:
    return ListView.from_dict(s)


def list_view_to_dict(x: ListView) -> Any:
    return to_class(ListView, x)


def offline_recommendations_remove_from_dict(s: Any) -> OfflineRecommendationsRemove:
    return OfflineRecommendationsRemove.from_dict(s)


def offline_recommendations_remove_to_dict(x: OfflineRecommendationsRemove) -> Any:
    return to_class(OfflineRecommendationsRemove, x)


def offline_recommendations_upsert_from_dict(s: Any) -> OfflineRecommendationsUpsert:
    return OfflineRecommendationsUpsert.from_dict(s)


def offline_recommendations_upsert_to_dict(x: OfflineRecommendationsUpsert) -> Any:
    return to_class(OfflineRecommendationsUpsert, x)


def other_interaction_from_dict(s: Any) -> OtherInteraction:
    return OtherInteraction.from_dict(s)


def other_interaction_to_dict(x: OtherInteraction) -> Any:
    return to_class(OtherInteraction, x)


def page_visit_from_dict(s: Any) -> PageVisit:
    return PageVisit.from_dict(s)


def page_visit_to_dict(x: PageVisit) -> Any:
    return to_class(PageVisit, x)


def placement_remove_from_dict(s: Any) -> PlacementRemove:
    return PlacementRemove.from_dict(s)


def placement_remove_to_dict(x: PlacementRemove) -> Any:
    return to_class(PlacementRemove, x)


def placement_upsert_from_dict(s: Any) -> PlacementUpsert:
    return PlacementUpsert.from_dict(s)


def placement_upsert_to_dict(x: PlacementUpsert) -> Any:
    return to_class(PlacementUpsert, x)


def purchase_complete_from_dict(s: Any) -> PurchaseComplete:
    return PurchaseComplete.from_dict(s)


def purchase_complete_to_dict(x: PurchaseComplete) -> Any:
    return to_class(PurchaseComplete, x)


def rate_product_from_dict(s: Any) -> RateProduct:
    return RateProduct.from_dict(s)


def rate_product_to_dict(x: RateProduct) -> Any:
    return to_class(RateProduct, x)


def reco_request_from_dict(s: Any) -> RecoRequest:
    return RecoRequest.from_dict(s)


def reco_request_to_dict(x: RecoRequest) -> Any:
    return to_class(RecoRequest, x)


def reco_show_from_dict(s: Any) -> RecoShow:
    return RecoShow.from_dict(s)


def reco_show_to_dict(x: RecoShow) -> Any:
    return to_class(RecoShow, x)


def remove_from_cart_from_dict(s: Any) -> RemoveFromCart:
    return RemoveFromCart.from_dict(s)


def remove_from_cart_to_dict(x: RemoveFromCart) -> Any:
    return to_class(RemoveFromCart, x)


def remove_from_list_from_dict(s: Any) -> RemoveFromList:
    return RemoveFromList.from_dict(s)


def remove_from_list_to_dict(x: RemoveFromList) -> Any:
    return to_class(RemoveFromList, x)


def search_items_from_dict(s: Any) -> SearchItems:
    return SearchItems.from_dict(s)


def search_items_to_dict(x: SearchItems) -> Any:
    return to_class(SearchItems, x)


def cart_page_view_from_dict(s: Any) -> CartPageView:
    return CartPageView.from_dict(s)


def cart_page_view_to_dict(x: CartPageView) -> Any:
    return to_class(CartPageView, x)


def smart_search_request_from_dict(s: Any) -> SmartSearchRequest:
    return SmartSearchRequest.from_dict(s)


def smart_search_request_to_dict(x: SmartSearchRequest) -> Any:
    return to_class(SmartSearchRequest, x)


def smart_search_show_from_dict(s: Any) -> SmartSearchShow:
    return SmartSearchShow.from_dict(s)


def smart_search_show_to_dict(x: SmartSearchShow) -> Any:
    return to_class(SmartSearchShow, x)


def sort_items_from_dict(s: Any) -> SortItems:
    return SortItems.from_dict(s)


def sort_items_to_dict(x: SortItems) -> Any:
    return to_class(SortItems, x)


def unknown_event_from_dict(s: Any) -> UnknownEvent:
    return UnknownEvent.from_dict(s)


def unknown_event_to_dict(x: UnknownEvent) -> Any:
    return to_class(UnknownEvent, x)
