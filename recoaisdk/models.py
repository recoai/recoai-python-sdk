# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = add_to_cart_from_dict(json.loads(json_string))
#     result = add_to_list_from_dict(json.loads(json_string))
#     result = api_settings_from_dict(json.loads(json_string))
#     result = builder_fn1_from_dict(json.loads(json_string))
#     result = builder_fn2_from_dict(json.loads(json_string))
#     result = builder_variable_from_dict(json.loads(json_string))
#     result = category_page_view_from_dict(json.loads(json_string))
#     result = change_item_stock_state_from_dict(json.loads(json_string))
#     result = checkout_start_from_dict(json.loads(json_string))
#     result = common_from_dict(json.loads(json_string))
#     result = detail_item_view_from_dict(json.loads(json_string))
#     result = home_page_view_from_dict(json.loads(json_string))
#     result = image_interaction_from_dict(json.loads(json_string))
#     result = item_attributes_selection_from_dict(json.loads(json_string))
#     result = item_remove_from_dict(json.loads(json_string))
#     result = items_impression_from_dict(json.loads(json_string))
#     result = items_view_from_dict(json.loads(json_string))
#     result = item_upsert_from_dict(json.loads(json_string))
#     result = list_view_from_dict(json.loads(json_string))
#     result = offline_recommendations_remove_from_dict(json.loads(json_string))
#     result = offline_recommendations_upsert_from_dict(json.loads(json_string))
#     result = other_interaction_from_dict(json.loads(json_string))
#     result = page_visit_from_dict(json.loads(json_string))
#     result = placement_remove_from_dict(json.loads(json_string))
#     result = placement_statistics_json_ready_from_dict(json.loads(json_string))
#     result = placement_upsert_from_dict(json.loads(json_string))
#     result = purchase_complete_from_dict(json.loads(json_string))
#     result = rate_item_from_dict(json.loads(json_string))
#     result = reco_ack_from_dict(json.loads(json_string))
#     result = reco_request_from_dict(json.loads(json_string))
#     result = reco_show_from_dict(json.loads(json_string))
#     result = remove_from_cart_from_dict(json.loads(json_string))
#     result = remove_from_list_from_dict(json.loads(json_string))
#     result = search_items_from_dict(json.loads(json_string))
#     result = cart_page_view_from_dict(json.loads(json_string))
#     result = smart_search_request_from_dict(json.loads(json_string))
#     result = smart_search_show_from_dict(json.loads(json_string))
#     result = sort_items_from_dict(json.loads(json_string))
#     result = strategy_parameters_types_from_dict(json.loads(json_string))
#     result = unknown_event_from_dict(json.loads(json_string))
#     result = video_interaction_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class EventDetail:
    url: str
    event_attributes: Optional[Dict[str, str]] = None
    experiment_ids: Optional[int] = None
    rec_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EventDetail':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        event_attributes = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("event_attributes"))
        experiment_ids = from_union([from_none, from_int], obj.get("experiment_ids"))
        rec_id = from_union([from_none, from_str], obj.get("rec_id"))
        return EventDetail(url, event_attributes, experiment_ids, rec_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["event_attributes"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.event_attributes)
        result["experiment_ids"] = from_union([from_none, from_int], self.experiment_ids)
        result["rec_id"] = from_union([from_none, from_str], self.rec_id)
        return result


class EventType(Enum):
    ADD_TO_CART = "AddToCart"
    ADD_TO_LIST = "AddToList"
    CART_PAGE_VIEW = "CartPageView"
    CHANGE_ITEM_STOCK_STATE = "ChangeItemStockState"
    CHECKOUT_START = "CheckoutStart"
    DETAIL_ITEM_VIEW = "DetailItemView"
    HOME_PAGE_VIEW = "HomePageView"
    IMAGE_INTERACTION = "ImageInteraction"
    ITEMS_VIEW = "ItemsView"
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
    RATE_ITEM = "RateItem"
    RECO_ACK = "RecoAck"
    RECO_REQUEST = "RecoRequest"
    RECO_SHOW = "RecoShow"
    REMOVE_FROM_CART = "RemoveFromCart"
    REMOVE_FROM_LIST = "RemoveFromList"
    SEARCH_ITEMS = "SearchItems"
    SMART_SEARCH_REQUEST = "SmartSearchRequest"
    SMART_SEARCH_SHOW = "SmartSearchShow"
    SORT_ITEMS = "SortItems"
    UNKNOWN_EVENT = "UnknownEvent"
    VIDEO_INTERACTION = "VideoInteraction"


@dataclass
class Article:
    author: str
    snippet: str
    timestamp_added: int

    @staticmethod
    def from_dict(obj: Any) -> 'Article':
        assert isinstance(obj, dict)
        author = from_str(obj.get("author"))
        snippet = from_str(obj.get("snippet"))
        timestamp_added = from_int(obj.get("timestamp_added"))
        return Article(author, snippet, timestamp_added)

    def to_dict(self) -> dict:
        result: dict = {}
        result["author"] = from_str(self.author)
        result["snippet"] = from_str(self.snippet)
        result["timestamp_added"] = from_int(self.timestamp_added)
        return result


@dataclass
class Categories:
    categories: List[List[Union[Dict[str, str], str]]]

    @staticmethod
    def from_dict(obj: Any) -> 'Categories':
        assert isinstance(obj, dict)
        categories = from_list(lambda x: from_list(lambda x: from_union([lambda x: from_dict(from_str, x), from_str], x), x), obj.get("categories"))
        return Categories(categories)

    def to_dict(self) -> dict:
        result: dict = {}
        result["categories"] = from_list(lambda x: from_list(lambda x: from_union([lambda x: from_dict(from_str, x), from_str], x), x), self.categories)
        return result


@dataclass
class Costs:
    costs: Dict[str, float]

    @staticmethod
    def from_dict(obj: Any) -> 'Costs':
        assert isinstance(obj, dict)
        costs = from_dict(from_float, obj.get("costs"))
        return Costs(costs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["costs"] = from_dict(to_float, self.costs)
        return result


@dataclass
class Description:
    content: Union[Dict[str, str], None, str]
    title: Union[Dict[str, str], str]
    language_code: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Description':
        assert isinstance(obj, dict)
        content = from_union([lambda x: from_dict(from_str, x), from_none, from_str], obj.get("content"))
        title = from_union([lambda x: from_dict(from_str, x), from_str], obj.get("title"))
        language_code = from_union([from_none, from_str], obj.get("language_code"))
        return Description(content, title, language_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content"] = from_union([lambda x: from_dict(from_str, x), from_none, from_str], self.content)
        result["title"] = from_union([lambda x: from_dict(from_str, x), from_str], self.title)
        result["language_code"] = from_union([from_none, from_str], self.language_code)
        return result


@dataclass
class ItemEcommerceSpec:
    item_code: Optional[str] = None
    item_group_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemEcommerceSpec':
        assert isinstance(obj, dict)
        item_code = from_union([from_none, from_str], obj.get("item_code"))
        item_group_id = from_union([from_none, from_str], obj.get("item_group_id"))
        return ItemEcommerceSpec(item_code, item_group_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["item_code"] = from_union([from_none, from_str], self.item_code)
        result["item_group_id"] = from_union([from_none, from_str], self.item_group_id)
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
class Images:
    images: List[Image]

    @staticmethod
    def from_dict(obj: Any) -> 'Images':
        assert isinstance(obj, dict)
        images = from_list(Image.from_dict, obj.get("images"))
        return Images(images)

    def to_dict(self) -> dict:
        result: dict = {}
        result["images"] = from_list(lambda x: to_class(Image, x), self.images)
        return result


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
class ExactPrice:
    display_price: float
    original_price: float
    currency_code: Optional[Currency] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ExactPrice':
        assert isinstance(obj, dict)
        display_price = from_float(obj.get("display_price"))
        original_price = from_float(obj.get("original_price"))
        currency_code = from_union([from_none, Currency], obj.get("currency_code"))
        return ExactPrice(display_price, original_price, currency_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["display_price"] = to_float(self.display_price)
        result["original_price"] = to_float(self.original_price)
        result["currency_code"] = from_union([from_none, lambda x: to_enum(Currency, x)], self.currency_code)
        return result


class StockState(Enum):
    BACK_ORDER = "BackOrder"
    IN_STOCK = "InStock"
    OUT_OF_STOCK = "OutOfStock"
    PRE_ORDER = "PreOrder"


@dataclass
class Stock:
    stock_state: StockState
    available_quantity: Optional[int] = None
    quantity: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Stock':
        assert isinstance(obj, dict)
        stock_state = StockState(obj.get("stock_state"))
        available_quantity = from_union([from_none, from_int], obj.get("available_quantity"))
        quantity = from_union([from_none, from_int], obj.get("quantity"))
        return Stock(stock_state, available_quantity, quantity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["stock_state"] = to_enum(StockState, self.stock_state)
        result["available_quantity"] = from_union([from_none, from_int], self.available_quantity)
        result["quantity"] = from_union([from_none, from_int], self.quantity)
        return result


@dataclass
class Tags:
    tags: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Tags':
        assert isinstance(obj, dict)
        tags = from_list(from_str, obj.get("tags"))
        return Tags(tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tags"] = from_list(from_str, self.tags)
        return result


@dataclass
class ItemURL:
    canonical_uri: str
    canonical_uri_with_params: Optional[str] = None
    url_params: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemURL':
        assert isinstance(obj, dict)
        canonical_uri = from_str(obj.get("canonical_uri"))
        canonical_uri_with_params = from_union([from_none, from_str], obj.get("canonical_uri_with_params"))
        url_params = from_union([from_none, from_str], obj.get("url_params"))
        return ItemURL(canonical_uri, canonical_uri_with_params, url_params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["canonical_uri"] = from_str(self.canonical_uri)
        result["canonical_uri_with_params"] = from_union([from_none, from_str], self.canonical_uri_with_params)
        result["url_params"] = from_union([from_none, from_str], self.url_params)
        return result


@dataclass
class Video:
    duration_secs: int
    uri: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        duration_secs = from_int(obj.get("duration_secs"))
        uri = from_union([from_none, from_str], obj.get("uri"))
        return Video(duration_secs, uri)

    def to_dict(self) -> dict:
        result: dict = {}
        result["duration_secs"] = from_int(self.duration_secs)
        result["uri"] = from_union([from_none, from_str], self.uri)
        return result


@dataclass
class Attributes:
    """This attribute structure is inspired by ECS dense components also know as table-based
    component list.
    """
    url: ItemURL
    article: Optional[Article] = None
    categories: Optional[Categories] = None
    costs: Optional[Costs] = None
    description: Optional[Description] = None
    ecommerce: Optional[ItemEcommerceSpec] = None
    images: Optional[Images] = None
    price: Optional[ExactPrice] = None
    stock: Optional[Stock] = None
    tags: Optional[Tags] = None
    video: Optional[Video] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Attributes':
        assert isinstance(obj, dict)
        url = ItemURL.from_dict(obj.get("url"))
        article = from_union([Article.from_dict, from_none], obj.get("article"))
        categories = from_union([Categories.from_dict, from_none], obj.get("categories"))
        costs = from_union([Costs.from_dict, from_none], obj.get("costs"))
        description = from_union([Description.from_dict, from_none], obj.get("description"))
        ecommerce = from_union([ItemEcommerceSpec.from_dict, from_none], obj.get("ecommerce"))
        images = from_union([Images.from_dict, from_none], obj.get("images"))
        price = from_union([ExactPrice.from_dict, from_none], obj.get("price"))
        stock = from_union([Stock.from_dict, from_none], obj.get("stock"))
        tags = from_union([Tags.from_dict, from_none], obj.get("tags"))
        video = from_union([Video.from_dict, from_none], obj.get("video"))
        return Attributes(url, article, categories, costs, description, ecommerce, images, price, stock, tags, video)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = to_class(ItemURL, self.url)
        result["article"] = from_union([lambda x: to_class(Article, x), from_none], self.article)
        result["categories"] = from_union([lambda x: to_class(Categories, x), from_none], self.categories)
        result["costs"] = from_union([lambda x: to_class(Costs, x), from_none], self.costs)
        result["description"] = from_union([lambda x: to_class(Description, x), from_none], self.description)
        result["ecommerce"] = from_union([lambda x: to_class(ItemEcommerceSpec, x), from_none], self.ecommerce)
        result["images"] = from_union([lambda x: to_class(Images, x), from_none], self.images)
        result["price"] = from_union([lambda x: to_class(ExactPrice, x), from_none], self.price)
        result["stock"] = from_union([lambda x: to_class(Stock, x), from_none], self.stock)
        result["tags"] = from_union([lambda x: to_class(Tags, x), from_none], self.tags)
        result["video"] = from_union([lambda x: to_class(Video, x), from_none], self.video)
        return result


class ItemType(Enum):
    ARTICLE = "Article"
    ECOMMERCE = "Ecommerce"
    UNKNOWN = "Unknown"
    VIDEO = "Video"


@dataclass
class ItemDetails:
    item_id: str
    item_type: ItemType
    attributes: Optional[Attributes] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemDetails':
        assert isinstance(obj, dict)
        item_id = from_str(obj.get("item_id"))
        item_type = ItemType(obj.get("item_type"))
        attributes = from_union([Attributes.from_dict, from_none], obj.get("attributes"))
        return ItemDetails(item_id, item_type, attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["item_id"] = from_str(self.item_id)
        result["item_type"] = to_enum(ItemType, self.item_type)
        result["attributes"] = from_union([lambda x: to_class(Attributes, x), from_none], self.attributes)
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


class PrivacySetting(Enum):
    NON_PERSONALIZED = "NonPersonalized"
    PERSONALIZED = "Personalized"


@dataclass
class UserInfo:
    visitor_id: str
    additional_info: Optional[UserAdditionalInfo] = None
    privacy_setting: Optional[PrivacySetting] = None
    session_id: Optional[str] = None
    user_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserInfo':
        assert isinstance(obj, dict)
        visitor_id = from_str(obj.get("visitor_id"))
        additional_info = from_union([UserAdditionalInfo.from_dict, from_none], obj.get("additional_info"))
        privacy_setting = from_union([from_none, PrivacySetting], obj.get("privacy_setting"))
        session_id = from_union([from_none, from_str], obj.get("session_id"))
        user_id = from_union([from_none, from_str], obj.get("user_id"))
        return UserInfo(visitor_id, additional_info, privacy_setting, session_id, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["visitor_id"] = from_str(self.visitor_id)
        result["additional_info"] = from_union([lambda x: to_class(UserAdditionalInfo, x), from_none], self.additional_info)
        result["privacy_setting"] = from_union([from_none, lambda x: to_enum(PrivacySetting, x)], self.privacy_setting)
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


class BuilderFn1(Enum):
    ARG_MAX = "ArgMax"
    ARG_MIN = "ArgMin"
    CONVERT_TO_PLACEMENT_ITEM_TYPE = "ConvertToPlacementItemType"
    INVERT = "Invert"
    RANKING = "Ranking"


class BuilderFn2(Enum):
    EXPAND = "Expand"
    HIGHEST = "Highest"
    INTERSECT = "Intersect"
    LESS = "Less"
    LESS_EQ = "LessEq"
    LOOKUP = "Lookup"
    LOWEST = "Lowest"
    MORE = "More"
    MORE_EQ = "MoreEq"
    REMOVE = "Remove"
    UNION = "Union"


class BuilderVariable(Enum):
    ALL_ITEMS = "AllItems"
    ITEMS_ALSO_ADDED_TO_CART_IN_SESSION = "ItemsAlsoAddedToCartInSession"
    ITEMS_ALSO_BOUGHT_IN_SESSION = "ItemsAlsoBoughtInSession"
    ITEMS_ALSO_SEEN_IN_SESSION = "ItemsAlsoSeenInSession"
    ITEMS_IN_CART = "ItemsInCart"
    ITEMS_RECOMMENDED_SESSION_COUNTER = "ItemsRecommendedSessionCounter"
    ITEMS_SEEN_IN_SESSION = "ItemsSeenInSession"
    ITEMS_VISITED_COUNTER = "ItemsVisitedCounter"
    ITEM_CURRENT = "ItemCurrent"
    ITEM_CURRENT_TYPE = "ItemCurrentType"


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


@dataclass
class Item:
    item_id: str
    item_type: ItemType

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        item_id = from_str(obj.get("item_id"))
        item_type = ItemType(obj.get("item_type"))
        return Item(item_id, item_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["item_id"] = from_str(self.item_id)
        result["item_type"] = to_enum(ItemType, self.item_type)
        return result


@dataclass
class ChangeItemStockState:
    event_type: EventType
    item: Item
    stock_state: StockState
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChangeItemStockState':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = Item.from_dict(obj.get("item"))
        stock_state = StockState(obj.get("stock_state"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return ChangeItemStockState(event_type, item, stock_state, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(Item, self.item)
        result["stock_state"] = to_enum(StockState, self.stock_state)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
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
class DetailItemViewAttributes:
    """Completed can mean for - video - whether someone watched the whole video - article -
    whether someone read the whole article
    """
    completed: Optional[bool] = None
    """This attribute can be used for different item types. For - Video - means watch time -
    Article - reading time - Ecommerce - time spend on viewing the product
    """
    view_time_secs: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DetailItemViewAttributes':
        assert isinstance(obj, dict)
        completed = from_union([from_none, from_bool], obj.get("completed"))
        view_time_secs = from_union([from_none, from_int], obj.get("view_time_secs"))
        return DetailItemViewAttributes(completed, view_time_secs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["completed"] = from_union([from_none, from_bool], self.completed)
        result["view_time_secs"] = from_union([from_none, from_int], self.view_time_secs)
        return result


@dataclass
class DetailItemView:
    event_type: EventType
    item: ItemDetails
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    rec_id: Optional[str] = None
    view_attributes: Optional[DetailItemViewAttributes] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DetailItemView':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        rec_id = from_union([from_none, from_str], obj.get("rec_id"))
        view_attributes = from_union([DetailItemViewAttributes.from_dict, from_none], obj.get("view_attributes"))
        return DetailItemView(event_type, item, user_info, event_detail, event_time, rec_id, view_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(ItemDetails, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["rec_id"] = from_union([from_none, from_str], self.rec_id)
        result["view_attributes"] = from_union([lambda x: to_class(DetailItemViewAttributes, x), from_none], self.view_attributes)
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


class ArticleFieldName(Enum):
    AUTHOR = "Author"
    SNIPPET = "Snippet"
    TIMESTAMP_ADDED = "TimestampAdded"


class CategoriesFieldName(Enum):
    CATEGORIES = "Categories"


class CostsFieldName(Enum):
    COSTS = "Costs"


class DescriptionFieldName(Enum):
    CONTENT = "Content"
    LANGUAGE_CODE = "LanguageCode"
    TITLE = "Title"


class ItemEcommerceSpecFieldName(Enum):
    ITEM_CODE = "ItemCode"
    ITEM_GROUP_ID = "ItemGroupId"


class ImagesFieldName(Enum):
    IMAGES = "Images"


class ExactPriceFieldName(Enum):
    CURRENCY_CODE = "CurrencyCode"
    DISPLAY_PRICE = "DisplayPrice"
    ORIGINAL_PRICE = "OriginalPrice"


class StockFieldName(Enum):
    AVAILABLE_QUANTITY = "AvailableQuantity"
    QUANTITY = "Quantity"
    STOCK_STATE = "StockState"


class TagsFieldName(Enum):
    TAGS = "Tags"


class ItemURLFieldName(Enum):
    CANONICAL_URI = "CanonicalUri"
    CANONICAL_URI_WITH_PARAMS = "CanonicalUriWithParams"
    URL_PARAMS = "UrlParams"


class VideoFieldName(Enum):
    DURATION_SECS = "DurationSecs"
    URI = "Uri"


@dataclass
class ItemAttributesFieldNames:
    url: Optional[ItemURLFieldName] = None
    price: Optional[ExactPriceFieldName] = None
    description: Optional[DescriptionFieldName] = None
    categories: Optional[CategoriesFieldName] = None
    images: Optional[ImagesFieldName] = None
    video: Optional[VideoFieldName] = None
    tags: Optional[TagsFieldName] = None
    article: Optional[ArticleFieldName] = None
    ecommerce_spec: Optional[ItemEcommerceSpecFieldName] = None
    stock: Optional[StockFieldName] = None
    costs: Optional[CostsFieldName] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemAttributesFieldNames':
        assert isinstance(obj, dict)
        url = from_union([ItemURLFieldName, from_none], obj.get("Url"))
        price = from_union([ExactPriceFieldName, from_none], obj.get("Price"))
        description = from_union([DescriptionFieldName, from_none], obj.get("Description"))
        categories = from_union([CategoriesFieldName, from_none], obj.get("Categories"))
        images = from_union([ImagesFieldName, from_none], obj.get("Images"))
        video = from_union([VideoFieldName, from_none], obj.get("Video"))
        tags = from_union([TagsFieldName, from_none], obj.get("Tags"))
        article = from_union([ArticleFieldName, from_none], obj.get("Article"))
        ecommerce_spec = from_union([ItemEcommerceSpecFieldName, from_none], obj.get("EcommerceSpec"))
        stock = from_union([StockFieldName, from_none], obj.get("Stock"))
        costs = from_union([CostsFieldName, from_none], obj.get("Costs"))
        return ItemAttributesFieldNames(url, price, description, categories, images, video, tags, article, ecommerce_spec, stock, costs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Url"] = from_union([lambda x: to_enum(ItemURLFieldName, x), from_none], self.url)
        result["Price"] = from_union([lambda x: to_enum(ExactPriceFieldName, x), from_none], self.price)
        result["Description"] = from_union([lambda x: to_enum(DescriptionFieldName, x), from_none], self.description)
        result["Categories"] = from_union([lambda x: to_enum(CategoriesFieldName, x), from_none], self.categories)
        result["Images"] = from_union([lambda x: to_enum(ImagesFieldName, x), from_none], self.images)
        result["Video"] = from_union([lambda x: to_enum(VideoFieldName, x), from_none], self.video)
        result["Tags"] = from_union([lambda x: to_enum(TagsFieldName, x), from_none], self.tags)
        result["Article"] = from_union([lambda x: to_enum(ArticleFieldName, x), from_none], self.article)
        result["EcommerceSpec"] = from_union([lambda x: to_enum(ItemEcommerceSpecFieldName, x), from_none], self.ecommerce_spec)
        result["Stock"] = from_union([lambda x: to_enum(StockFieldName, x), from_none], self.stock)
        result["Costs"] = from_union([lambda x: to_enum(CostsFieldName, x), from_none], self.costs)
        return result


@dataclass
class ItemAttributesSelectionClass:
    selected_attributes: List[ItemAttributesFieldNames]

    @staticmethod
    def from_dict(obj: Any) -> 'ItemAttributesSelectionClass':
        assert isinstance(obj, dict)
        selected_attributes = from_list(ItemAttributesFieldNames.from_dict, obj.get("SelectedAttributes"))
        return ItemAttributesSelectionClass(selected_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SelectedAttributes"] = from_list(lambda x: to_class(ItemAttributesFieldNames, x), self.selected_attributes)
        return result


class ItemAttributesSelectionEnum(Enum):
    ALL_ATTRIBUTES = "AllAttributes"


@dataclass
class ItemRemove:
    event_type: EventType
    item: Item
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemRemove':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = Item.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return ItemRemove(event_type, item, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item"] = to_class(Item, self.item)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


@dataclass
class ItemsImpression:
    event_type: EventType
    items: List[ItemDetails]
    on_screen: bool
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    page_categories: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemsImpression':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        on_screen = from_bool(obj.get("on_screen"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        page_categories = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("page_categories"))
        return ItemsImpression(event_type, items, on_screen, user_info, event_detail, event_time, page_categories)

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


@dataclass
class ItemsView:
    event_type: EventType
    items: List[ItemDetails]
    on_screen: bool
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    page_categories: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemsView':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        on_screen = from_bool(obj.get("on_screen"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        page_categories = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("page_categories"))
        return ItemsView(event_type, items, on_screen, user_info, event_detail, event_time, page_categories)

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


@dataclass
class ItemUpsert:
    event_type: EventType
    item_details: ItemDetails
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemUpsert':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item_details = ItemDetails.from_dict(obj.get("item_details"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return ItemUpsert(event_type, item_details, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item_details"] = to_class(ItemDetails, self.item_details)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
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
    ATTRIBUTES_SIMILARITY = "AttributesSimilarity"
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


@dataclass
class LIFOVecForUint128:
    base: List[int]
    capacity: int

    @staticmethod
    def from_dict(obj: Any) -> 'LIFOVecForUint128':
        assert isinstance(obj, dict)
        base = from_list(from_int, obj.get("base"))
        capacity = from_int(obj.get("capacity"))
        return LIFOVecForUint128(base, capacity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["base"] = from_list(from_int, self.base)
        result["capacity"] = from_int(self.capacity)
        return result


class GenericStrategy(Enum):
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


@dataclass
class SuccessTriesClass:
    """Pre-defined strategies
    
    Build your custom strategies
    
    Similar description, image or other defined by you
    """
    similarities: Union[OfflineRecommendationsTypeClass, OfflineRecommendationsTypeEnum, None]
    generic: Optional[GenericStrategy] = None
    strategy_builder: Optional[str] = None
    n_impressions: Optional[int] = None
    n_success: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SuccessTriesClass':
        assert isinstance(obj, dict)
        similarities = from_union([OfflineRecommendationsTypeClass.from_dict, OfflineRecommendationsTypeEnum, from_none], obj.get("Similarities"))
        generic = from_union([GenericStrategy, from_none], obj.get("Generic"))
        strategy_builder = from_union([from_str, from_none], obj.get("StrategyBuilder"))
        n_impressions = from_union([from_int, from_none], obj.get("n_impressions"))
        n_success = from_union([from_int, from_none], obj.get("n_success"))
        return SuccessTriesClass(similarities, generic, strategy_builder, n_impressions, n_success)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Similarities"] = from_union([lambda x: to_class(OfflineRecommendationsTypeClass, x), lambda x: to_enum(OfflineRecommendationsTypeEnum, x), from_none], self.similarities)
        result["Generic"] = from_union([lambda x: to_enum(GenericStrategy, x), from_none], self.generic)
        result["StrategyBuilder"] = from_union([from_str, from_none], self.strategy_builder)
        result["n_impressions"] = from_union([from_int, from_none], self.n_impressions)
        result["n_success"] = from_union([from_int, from_none], self.n_success)
        return result


class StrategyEnum(Enum):
    UNKNOWN = "Unknown"


@dataclass
class PlacementStatisticsJSONReady:
    """Json safe version of PlacementStatistics, unfortunately serde_with doesn't work because
    of conflicts with JsonSchema
    """
    loading_times_microseconds: Dict[str, LIFOVecForUint128]
    placements_statistics: Dict[str, List[List[Union[SuccessTriesClass, StrategyEnum]]]]

    @staticmethod
    def from_dict(obj: Any) -> 'PlacementStatisticsJSONReady':
        assert isinstance(obj, dict)
        loading_times_microseconds = from_dict(LIFOVecForUint128.from_dict, obj.get("loading_times_microseconds"))
        placements_statistics = from_dict(lambda x: from_list(lambda x: from_list(lambda x: from_union([SuccessTriesClass.from_dict, StrategyEnum], x), x), x), obj.get("placements_statistics"))
        return PlacementStatisticsJSONReady(loading_times_microseconds, placements_statistics)

    def to_dict(self) -> dict:
        result: dict = {}
        result["loading_times_microseconds"] = from_dict(lambda x: to_class(LIFOVecForUint128, x), self.loading_times_microseconds)
        result["placements_statistics"] = from_dict(lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(SuccessTriesClass, x), lambda x: to_enum(StrategyEnum, x)], x), x), x), self.placements_statistics)
        return result


class Location(Enum):
    """Choose location"""
    ADD_TO_CART = "AddToCart"
    CATEGORY_PAGE = "CategoryPage"
    CHECKOUT_PAGE = "CheckoutPage"
    ERROR404 = "Error404"
    HOME_PAGE = "HomePage"
    ITEM_PAGE = "ItemPage"
    OTHER_PAGE = "OtherPage"
    SEARCH_PAGE = "SearchPage"
    UNKNOWN_PAGE = "UnknownPage"


class StrategySelectorStrategyChooseOne(Enum):
    """How the strategies are selected"""
    RANKING_MODEL = "RankingModel"
    THOMPSON_SAMPLING = "ThompsonSampling"
    WEIGHTED_SAMPLE = "WeightedSample"


@dataclass
class StrategyGenericStrategies:
    """Pre-defined strategies
    
    Build your custom strategies
    
    Similar description, image or other defined by you
    """
    similarities: Union[OfflineRecommendationsTypeClass, OfflineRecommendationsTypeEnum, None]
    generic: Optional[GenericStrategy] = None
    strategy_builder: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StrategyGenericStrategies':
        assert isinstance(obj, dict)
        similarities = from_union([OfflineRecommendationsTypeClass.from_dict, OfflineRecommendationsTypeEnum, from_none], obj.get("Similarities"))
        generic = from_union([GenericStrategy, from_none], obj.get("Generic"))
        strategy_builder = from_union([from_str, from_none], obj.get("StrategyBuilder"))
        return StrategyGenericStrategies(similarities, generic, strategy_builder)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Similarities"] = from_union([lambda x: to_class(OfflineRecommendationsTypeClass, x), lambda x: to_enum(OfflineRecommendationsTypeEnum, x), from_none], self.similarities)
        result["Generic"] = from_union([lambda x: to_enum(GenericStrategy, x), from_none], self.generic)
        result["StrategyBuilder"] = from_union([from_str, from_none], self.strategy_builder)
        return result


@dataclass
class WeightedGenericCandidateRec:
    strategy: Union[StrategyGenericStrategies, StrategyEnum]
    weight: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WeightedGenericCandidateRec':
        assert isinstance(obj, dict)
        strategy = from_union([StrategyGenericStrategies.from_dict, StrategyEnum], obj.get("strategy"))
        weight = from_union([from_none, from_float], obj.get("weight"))
        return WeightedGenericCandidateRec(strategy, weight)

    def to_dict(self) -> dict:
        result: dict = {}
        result["strategy"] = from_union([lambda x: to_class(StrategyGenericStrategies, x), lambda x: to_enum(StrategyEnum, x)], self.strategy)
        result["weight"] = from_union([from_none, to_float], self.weight)
        return result


@dataclass
class PlacementUpsert:
    event_type: EventType
    item_type: ItemType
    """Lowercase no spaces allowed"""
    name: str
    """How the strategies are selected"""
    ranking: StrategySelectorStrategyChooseOne
    strategies: List[WeightedGenericCandidateRec]
    user_info: UserInfo
    enabled: Optional[bool] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    html_template: Optional[str] = None
    location: Optional[Location] = None
    url_params: Optional[Dict[str, str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlacementUpsert':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item_type = ItemType(obj.get("item_type"))
        name = from_str(obj.get("name"))
        ranking = StrategySelectorStrategyChooseOne(obj.get("ranking"))
        strategies = from_list(WeightedGenericCandidateRec.from_dict, obj.get("strategies"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        enabled = from_union([from_none, from_bool], obj.get("enabled"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        html_template = from_union([from_none, from_str], obj.get("html_template"))
        location = from_union([from_none, Location], obj.get("location"))
        url_params = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("url_params"))
        return PlacementUpsert(event_type, item_type, name, ranking, strategies, user_info, enabled, event_detail, event_time, html_template, location, url_params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["item_type"] = to_enum(ItemType, self.item_type)
        result["name"] = from_str(self.name)
        result["ranking"] = to_enum(StrategySelectorStrategyChooseOne, self.ranking)
        result["strategies"] = from_list(lambda x: to_class(WeightedGenericCandidateRec, x), self.strategies)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["enabled"] = from_union([from_none, from_bool], self.enabled)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["html_template"] = from_union([from_none, from_str], self.html_template)
        result["location"] = from_union([from_none, lambda x: to_enum(Location, x)], self.location)
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
class RateItem:
    event_type: EventType
    item: ItemDetails
    user_info: UserInfo
    comment: Optional[str] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    rating: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RateItem':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        item = ItemDetails.from_dict(obj.get("item"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        comment = from_union([from_none, from_str], obj.get("comment"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        rating = from_union([from_none, from_float], obj.get("rating"))
        return RateItem(event_type, item, user_info, comment, event_detail, event_time, rating)

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
class StrategiesUsedGenericStrategies:
    """Pre-defined strategies
    
    Build your custom strategies
    
    Similar description, image or other defined by you
    """
    similarities: Union[OfflineRecommendationsTypeClass, OfflineRecommendationsTypeEnum, None]
    generic: Optional[GenericStrategy] = None
    strategy_builder: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StrategiesUsedGenericStrategies':
        assert isinstance(obj, dict)
        similarities = from_union([OfflineRecommendationsTypeClass.from_dict, OfflineRecommendationsTypeEnum, from_none], obj.get("Similarities"))
        generic = from_union([GenericStrategy, from_none], obj.get("Generic"))
        strategy_builder = from_union([from_str, from_none], obj.get("StrategyBuilder"))
        return StrategiesUsedGenericStrategies(similarities, generic, strategy_builder)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Similarities"] = from_union([lambda x: to_class(OfflineRecommendationsTypeClass, x), lambda x: to_enum(OfflineRecommendationsTypeEnum, x), from_none], self.similarities)
        result["Generic"] = from_union([lambda x: to_enum(GenericStrategy, x), from_none], self.generic)
        result["StrategyBuilder"] = from_union([from_str, from_none], self.strategy_builder)
        return result


@dataclass
class ItemDetailsRecoShow:
    """Note that ItemDetailsRecoShow is already translated"""
    attributes: Attributes
    item: Item
    rec_id: str
    strategy_selected: Union[StrategyGenericStrategies, StrategyEnum]
    score: Optional[float] = None
    strategies_used: Optional[List[List[Union[StrategiesUsedGenericStrategies, float, StrategyEnum]]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemDetailsRecoShow':
        assert isinstance(obj, dict)
        attributes = Attributes.from_dict(obj.get("attributes"))
        item = Item.from_dict(obj.get("item"))
        rec_id = from_str(obj.get("rec_id"))
        strategy_selected = from_union([StrategyGenericStrategies.from_dict, StrategyEnum], obj.get("strategy_selected"))
        score = from_union([from_none, from_float], obj.get("score"))
        strategies_used = from_union([from_none, lambda x: from_list(lambda x: from_list(lambda x: from_union([StrategiesUsedGenericStrategies.from_dict, from_float, StrategyEnum], x), x), x)], obj.get("strategies_used"))
        return ItemDetailsRecoShow(attributes, item, rec_id, strategy_selected, score, strategies_used)

    def to_dict(self) -> dict:
        result: dict = {}
        result["attributes"] = to_class(Attributes, self.attributes)
        result["item"] = to_class(Item, self.item)
        result["rec_id"] = from_str(self.rec_id)
        result["strategy_selected"] = from_union([lambda x: to_class(StrategyGenericStrategies, x), lambda x: to_enum(StrategyEnum, x)], self.strategy_selected)
        result["score"] = from_union([from_none, to_float], self.score)
        result["strategies_used"] = from_union([from_none, lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(StrategiesUsedGenericStrategies, x), to_float, lambda x: to_enum(StrategyEnum, x)], x), x), x)], self.strategies_used)
        return result


@dataclass
class ItemAttributesSelectionItemAttributesSelectionClass:
    selected_attributes: List[ItemAttributesFieldNames]

    @staticmethod
    def from_dict(obj: Any) -> 'ItemAttributesSelectionItemAttributesSelectionClass':
        assert isinstance(obj, dict)
        selected_attributes = from_list(ItemAttributesFieldNames.from_dict, obj.get("SelectedAttributes"))
        return ItemAttributesSelectionItemAttributesSelectionClass(selected_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SelectedAttributes"] = from_list(lambda x: to_class(ItemAttributesFieldNames, x), self.selected_attributes)
        return result


@dataclass
class PageInfo:
    """Set page content"""
    content: Optional[str] = None
    """Item type"""
    item_type: Optional[ItemType] = None
    """Set page URL"""
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PageInfo':
        assert isinstance(obj, dict)
        content = from_union([from_none, from_str], obj.get("content"))
        item_type = from_union([from_none, ItemType], obj.get("item_type"))
        url = from_union([from_none, from_str], obj.get("url"))
        return PageInfo(content, item_type, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content"] = from_union([from_none, from_str], self.content)
        result["item_type"] = from_union([from_none, lambda x: to_enum(ItemType, x)], self.item_type)
        result["url"] = from_union([from_none, from_str], self.url)
        return result


@dataclass
class SearchInfo:
    """Set the search query"""
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
class StrategyParametersValues:
    additional_int_params: Optional[Dict[str, int]] = None
    additional_str_params: Optional[Dict[str, str]] = None
    category_id: Optional[List[str]] = None
    category_ids: Optional[List[List[str]]] = None
    item: Optional[Item] = None
    items: Optional[List[Item]] = None
    page_info: Optional[PageInfo] = None
    search_info: Optional[SearchInfo] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StrategyParametersValues':
        assert isinstance(obj, dict)
        additional_int_params = from_union([from_none, lambda x: from_dict(from_int, x)], obj.get("additional_int_params"))
        additional_str_params = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("additional_str_params"))
        category_id = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("category_id"))
        category_ids = from_union([from_none, lambda x: from_list(lambda x: from_list(from_str, x), x)], obj.get("category_ids"))
        item = from_union([Item.from_dict, from_none], obj.get("item"))
        items = from_union([from_none, lambda x: from_list(Item.from_dict, x)], obj.get("items"))
        page_info = from_union([PageInfo.from_dict, from_none], obj.get("page_info"))
        search_info = from_union([SearchInfo.from_dict, from_none], obj.get("search_info"))
        return StrategyParametersValues(additional_int_params, additional_str_params, category_id, category_ids, item, items, page_info, search_info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["additional_int_params"] = from_union([from_none, lambda x: from_dict(from_int, x)], self.additional_int_params)
        result["additional_str_params"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.additional_str_params)
        result["category_id"] = from_union([from_none, lambda x: from_list(from_str, x)], self.category_id)
        result["category_ids"] = from_union([from_none, lambda x: from_list(lambda x: from_list(from_str, x), x)], self.category_ids)
        result["item"] = from_union([lambda x: to_class(Item, x), from_none], self.item)
        result["items"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Item, x), x)], self.items)
        result["page_info"] = from_union([lambda x: to_class(PageInfo, x), from_none], self.page_info)
        result["search_info"] = from_union([lambda x: to_class(SearchInfo, x), from_none], self.search_info)
        return result


@dataclass
class PlacementConfig:
    item_attributes_selection: Union[ItemAttributesSelectionItemAttributesSelectionClass, ItemAttributesSelectionEnum, None]
    item_type: ItemType
    name: str
    html_template: Optional[str] = None
    location: Optional[Location] = None
    parameters: Optional[StrategyParametersValues] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlacementConfig':
        assert isinstance(obj, dict)
        item_attributes_selection = from_union([ItemAttributesSelectionItemAttributesSelectionClass.from_dict, from_none, ItemAttributesSelectionEnum], obj.get("item_attributes_selection"))
        item_type = ItemType(obj.get("item_type"))
        name = from_str(obj.get("name"))
        html_template = from_union([from_none, from_str], obj.get("html_template"))
        location = from_union([from_none, Location], obj.get("location"))
        parameters = from_union([StrategyParametersValues.from_dict, from_none], obj.get("parameters"))
        return PlacementConfig(item_attributes_selection, item_type, name, html_template, location, parameters)

    def to_dict(self) -> dict:
        result: dict = {}
        result["item_attributes_selection"] = from_union([lambda x: to_class(ItemAttributesSelectionItemAttributesSelectionClass, x), from_none, lambda x: to_enum(ItemAttributesSelectionEnum, x)], self.item_attributes_selection)
        result["item_type"] = to_enum(ItemType, self.item_type)
        result["name"] = from_str(self.name)
        result["html_template"] = from_union([from_none, from_str], self.html_template)
        result["location"] = from_union([from_none, lambda x: to_enum(Location, x)], self.location)
        result["parameters"] = from_union([lambda x: to_class(StrategyParametersValues, x), from_none], self.parameters)
        return result


@dataclass
class RecoACK:
    event_type: EventType
    items: List[ItemDetailsRecoShow]
    placement_config: PlacementConfig
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecoACK':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetailsRecoShow.from_dict, obj.get("items"))
        placement_config = PlacementConfig.from_dict(obj.get("placement_config"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return RecoACK(event_type, items, placement_config, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetailsRecoShow, x), self.items)
        result["placement_config"] = to_class(PlacementConfig, self.placement_config)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        return result


class Locale(Enum):
    AF_ZA = "af_ZA"
    AR_AR = "ar_AR"
    AS_IN = "as_IN"
    AZ_AZ = "az_AZ"
    BE_BY = "be_BY"
    BG_BG = "bg_BG"
    BN_IN = "bn_IN"
    BR_FR = "br_FR"
    BS_BA = "bs_BA"
    CA_ES = "ca_ES"
    CB_IQ = "cb_IQ"
    CO_FR = "co_FR"
    CS_CZ = "cs_CZ"
    CX_PH = "cx_PH"
    CY_GB = "cy_GB"
    DA_DK = "da_DK"
    DE_DE = "de_DE"
    EL_GR = "el_GR"
    EN_GB = "en_GB"
    EN_UD = "en_UD"
    EN_US = "en_US"
    ES_ES = "es_ES"
    ES_LA = "es_LA"
    ET_EE = "et_EE"
    EU_ES = "eu_ES"
    FA_IR = "fa_IR"
    FF_NG = "ff_NG"
    FI_FI = "fi_FI"
    FO_FO = "fo_FO"
    FR_CA = "fr_CA"
    FR_FR = "fr_FR"
    FY_NL = "fy_NL"
    GA_IE = "ga_IE"
    GL_ES = "gl_ES"
    GN_PY = "gn_PY"
    GU_IN = "gu_IN"
    HA_NG = "ha_NG"
    HE_IL = "he_IL"
    HI_IN = "hi_IN"
    HR_HR = "hr_HR"
    HU_HU = "hu_HU"
    HY_AM = "hy_AM"
    ID_ID = "id_ID"
    IS_IS = "is_IS"
    IT_IT = "it_IT"
    JA_JP = "ja_JP"
    JA_KS = "ja_KS"
    JV_ID = "jv_ID"
    KA_GE = "ka_GE"
    KK_KZ = "kk_KZ"
    KM_KH = "km_KH"
    KN_IN = "kn_IN"
    KO_KR = "ko_KR"
    KU_TR = "ku_TR"
    LT_LT = "lt_LT"
    LV_LV = "lv_LV"
    MG_MG = "mg_MG"
    MK_MK = "mk_MK"
    ML_IN = "ml_IN"
    MN_MN = "mn_MN"
    MR_IN = "mr_IN"
    MS_MY = "ms_MY"
    MT_MT = "mt_MT"
    MY_MM = "my_MM"
    NB_NO = "nb_NO"
    NE_NP = "ne_NP"
    NL_BE = "nl_BE"
    NL_NL = "nl_NL"
    NN_NO = "nn_NO"
    OR_IN = "or_IN"
    PA_IN = "pa_IN"
    PL_PL = "pl_PL"
    PS_AF = "ps_AF"
    PT_BR = "pt_BR"
    PT_PT = "pt_PT"
    QZ_MM = "qz_MM"
    RO_RO = "ro_RO"
    RU_RU = "ru_RU"
    RW_RW = "rw_RW"
    SC_IT = "sc_IT"
    SI_LK = "si_LK"
    SK_SK = "sk_SK"
    SL_SI = "sl_SI"
    SO_SO = "so_SO"
    SQ_AL = "sq_AL"
    SR_RS = "sr_RS"
    SV_SE = "sv_SE"
    SW_KE = "sw_KE"
    SZ_PL = "sz_PL"
    TA_IN = "ta_IN"
    TE_IN = "te_IN"
    TG_TJ = "tg_TJ"
    TH_TH = "th_TH"
    TL_PH = "tl_PH"
    TR_TR = "tr_TR"
    TZ_MA = "tz_MA"
    UK_UA = "uk_UA"
    UR_PK = "ur_PK"
    UZ_UZ = "uz_UZ"
    VI_VN = "vi_VN"
    ZH_CN = "zh_CN"
    ZH_HK = "zh_HK"
    ZH_TW = "zh_TW"


@dataclass
class RecoRequest:
    event_type: EventType
    location: Location
    n_items: int
    placement_config: PlacementConfig
    user_info: UserInfo
    additional_uri_params: Optional[Dict[str, str]] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    locale: Optional[Locale] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecoRequest':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        location = Location(obj.get("location"))
        n_items = from_int(obj.get("n_items"))
        placement_config = PlacementConfig.from_dict(obj.get("placement_config"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        additional_uri_params = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("additional_uri_params"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        locale = from_union([from_none, Locale], obj.get("locale"))
        return RecoRequest(event_type, location, n_items, placement_config, user_info, additional_uri_params, event_detail, event_time, locale)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["location"] = to_enum(Location, self.location)
        result["n_items"] = from_int(self.n_items)
        result["placement_config"] = to_class(PlacementConfig, self.placement_config)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["additional_uri_params"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.additional_uri_params)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["locale"] = from_union([from_none, lambda x: to_enum(Locale, x)], self.locale)
        return result


@dataclass
class RecoShow:
    event_type: EventType
    items: List[ItemDetailsRecoShow]
    placement_config: PlacementConfig
    user_info: UserInfo
    additional_uri_params: Optional[Dict[str, str]] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    experiment_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecoShow':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetailsRecoShow.from_dict, obj.get("items"))
        placement_config = PlacementConfig.from_dict(obj.get("placement_config"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        additional_uri_params = from_union([from_none, lambda x: from_dict(from_str, x)], obj.get("additional_uri_params"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        experiment_id = from_union([from_none, from_str], obj.get("experiment_id"))
        return RecoShow(event_type, items, placement_config, user_info, additional_uri_params, event_detail, event_time, experiment_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetailsRecoShow, x), self.items)
        result["placement_config"] = to_class(PlacementConfig, self.placement_config)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["additional_uri_params"] = from_union([from_none, lambda x: from_dict(from_str, x)], self.additional_uri_params)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["experiment_id"] = from_union([from_none, from_str], self.experiment_id)
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
    items: List[ItemDetailsRecoShow]
    user_info: UserInfo
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SmartSearchShow':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetailsRecoShow.from_dict, obj.get("items"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        return SmartSearchShow(event_type, items, user_info, event_detail, event_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetailsRecoShow, x), self.items)
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
class StrategyParametersTypes:
    category_id: bool
    category_ids: bool
    item: bool
    items_info: bool
    page_info: bool
    search_info: bool
    additional_int_params: Optional[List[str]] = None
    additional_str_params: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StrategyParametersTypes':
        assert isinstance(obj, dict)
        category_id = from_bool(obj.get("category_id"))
        category_ids = from_bool(obj.get("category_ids"))
        item = from_bool(obj.get("item"))
        items_info = from_bool(obj.get("items_info"))
        page_info = from_bool(obj.get("page_info"))
        search_info = from_bool(obj.get("search_info"))
        additional_int_params = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("additional_int_params"))
        additional_str_params = from_union([from_none, lambda x: from_list(from_str, x)], obj.get("additional_str_params"))
        return StrategyParametersTypes(category_id, category_ids, item, items_info, page_info, search_info, additional_int_params, additional_str_params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["category_id"] = from_bool(self.category_id)
        result["category_ids"] = from_bool(self.category_ids)
        result["item"] = from_bool(self.item)
        result["items_info"] = from_bool(self.items_info)
        result["page_info"] = from_bool(self.page_info)
        result["search_info"] = from_bool(self.search_info)
        result["additional_int_params"] = from_union([from_none, lambda x: from_list(from_str, x)], self.additional_int_params)
        result["additional_str_params"] = from_union([from_none, lambda x: from_list(from_str, x)], self.additional_str_params)
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


@dataclass
class VideoInteraction:
    event_type: EventType
    items: List[ItemDetails]
    user_info: UserInfo
    completed: Optional[bool] = None
    event_detail: Optional[EventDetail] = None
    event_time: Optional[int] = None
    video_item: Optional[Item] = None
    watched_secs: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VideoInteraction':
        assert isinstance(obj, dict)
        event_type = EventType(obj.get("event_type"))
        items = from_list(ItemDetails.from_dict, obj.get("items"))
        user_info = UserInfo.from_dict(obj.get("user_info"))
        completed = from_union([from_none, from_bool], obj.get("completed"))
        event_detail = from_union([EventDetail.from_dict, from_none], obj.get("event_detail"))
        event_time = from_union([from_none, from_int], obj.get("event_time"))
        video_item = from_union([Item.from_dict, from_none], obj.get("video_item"))
        watched_secs = from_union([from_none, from_int], obj.get("watched_secs"))
        return VideoInteraction(event_type, items, user_info, completed, event_detail, event_time, video_item, watched_secs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["event_type"] = to_enum(EventType, self.event_type)
        result["items"] = from_list(lambda x: to_class(ItemDetails, x), self.items)
        result["user_info"] = to_class(UserInfo, self.user_info)
        result["completed"] = from_union([from_none, from_bool], self.completed)
        result["event_detail"] = from_union([lambda x: to_class(EventDetail, x), from_none], self.event_detail)
        result["event_time"] = from_union([from_none, from_int], self.event_time)
        result["video_item"] = from_union([lambda x: to_class(Item, x), from_none], self.video_item)
        result["watched_secs"] = from_union([from_none, from_int], self.watched_secs)
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


def builder_fn1_from_dict(s: Any) -> BuilderFn1:
    return BuilderFn1(s)


def builder_fn1_to_dict(x: BuilderFn1) -> Any:
    return to_enum(BuilderFn1, x)


def builder_fn2_from_dict(s: Any) -> BuilderFn2:
    return BuilderFn2(s)


def builder_fn2_to_dict(x: BuilderFn2) -> Any:
    return to_enum(BuilderFn2, x)


def builder_variable_from_dict(s: Any) -> BuilderVariable:
    return BuilderVariable(s)


def builder_variable_to_dict(x: BuilderVariable) -> Any:
    return to_enum(BuilderVariable, x)


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


def detail_item_view_from_dict(s: Any) -> DetailItemView:
    return DetailItemView.from_dict(s)


def detail_item_view_to_dict(x: DetailItemView) -> Any:
    return to_class(DetailItemView, x)


def home_page_view_from_dict(s: Any) -> HomePageView:
    return HomePageView.from_dict(s)


def home_page_view_to_dict(x: HomePageView) -> Any:
    return to_class(HomePageView, x)


def image_interaction_from_dict(s: Any) -> ImageInteraction:
    return ImageInteraction.from_dict(s)


def image_interaction_to_dict(x: ImageInteraction) -> Any:
    return to_class(ImageInteraction, x)


def item_attributes_selection_from_dict(s: Any) -> Union[ItemAttributesSelectionClass, ItemAttributesSelectionEnum]:
    return from_union([ItemAttributesSelectionClass.from_dict, ItemAttributesSelectionEnum], s)


def item_attributes_selection_to_dict(x: Union[ItemAttributesSelectionClass, ItemAttributesSelectionEnum]) -> Any:
    return from_union([lambda x: to_class(ItemAttributesSelectionClass, x), lambda x: to_enum(ItemAttributesSelectionEnum, x)], x)


def item_remove_from_dict(s: Any) -> ItemRemove:
    return ItemRemove.from_dict(s)


def item_remove_to_dict(x: ItemRemove) -> Any:
    return to_class(ItemRemove, x)


def items_impression_from_dict(s: Any) -> ItemsImpression:
    return ItemsImpression.from_dict(s)


def items_impression_to_dict(x: ItemsImpression) -> Any:
    return to_class(ItemsImpression, x)


def items_view_from_dict(s: Any) -> ItemsView:
    return ItemsView.from_dict(s)


def items_view_to_dict(x: ItemsView) -> Any:
    return to_class(ItemsView, x)


def item_upsert_from_dict(s: Any) -> ItemUpsert:
    return ItemUpsert.from_dict(s)


def item_upsert_to_dict(x: ItemUpsert) -> Any:
    return to_class(ItemUpsert, x)


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


def placement_statistics_json_ready_from_dict(s: Any) -> PlacementStatisticsJSONReady:
    return PlacementStatisticsJSONReady.from_dict(s)


def placement_statistics_json_ready_to_dict(x: PlacementStatisticsJSONReady) -> Any:
    return to_class(PlacementStatisticsJSONReady, x)


def placement_upsert_from_dict(s: Any) -> PlacementUpsert:
    return PlacementUpsert.from_dict(s)


def placement_upsert_to_dict(x: PlacementUpsert) -> Any:
    return to_class(PlacementUpsert, x)


def purchase_complete_from_dict(s: Any) -> PurchaseComplete:
    return PurchaseComplete.from_dict(s)


def purchase_complete_to_dict(x: PurchaseComplete) -> Any:
    return to_class(PurchaseComplete, x)


def rate_item_from_dict(s: Any) -> RateItem:
    return RateItem.from_dict(s)


def rate_item_to_dict(x: RateItem) -> Any:
    return to_class(RateItem, x)


def reco_ack_from_dict(s: Any) -> RecoACK:
    return RecoACK.from_dict(s)


def reco_ack_to_dict(x: RecoACK) -> Any:
    return to_class(RecoACK, x)


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


def strategy_parameters_types_from_dict(s: Any) -> StrategyParametersTypes:
    return StrategyParametersTypes.from_dict(s)


def strategy_parameters_types_to_dict(x: StrategyParametersTypes) -> Any:
    return to_class(StrategyParametersTypes, x)


def unknown_event_from_dict(s: Any) -> UnknownEvent:
    return UnknownEvent.from_dict(s)


def unknown_event_to_dict(x: UnknownEvent) -> Any:
    return to_class(UnknownEvent, x)


def video_interaction_from_dict(s: Any) -> VideoInteraction:
    return VideoInteraction.from_dict(s)


def video_interaction_to_dict(x: VideoInteraction) -> Any:
    return to_class(VideoInteraction, x)
