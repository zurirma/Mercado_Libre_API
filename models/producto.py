from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class ValueStructItem(BaseModel):
    number: int
    unit: str


class StructItem(BaseModel):
    number: int
    unit: str


class Value(BaseModel):
    id: Optional[str]
    name: str
    struct: Optional[StructItem]


class SaleTerm(BaseModel):
    id: str
    name: str
    value_id: Optional[str]
    value_name: str
    value_struct: Optional[ValueStructItem]
    values: List[Value]


class Picture(BaseModel):
    id: str
    url: str
    secure_url: str
    size: str
    max_size: str
    quality: str


class Description(BaseModel):
    id: str


class Rule(BaseModel):
    default: bool
    free_mode: str
    free_shipping_flag: bool
    value: Any


class FreeMethod(BaseModel):
    id: int
    rule: Rule


class Shipping(BaseModel):
    mode: str
    free_methods: List[FreeMethod]
    tags: List[str]
    dimensions: Any
    local_pick_up: bool
    free_shipping: bool
    logistic_type: str
    store_pick_up: bool


class City(BaseModel):
    name: str


class State(BaseModel):
    id: str
    name: str


class Country(BaseModel):
    id: str
    name: str


class Neighborhood(BaseModel):
    id: str
    name: str


class City1(BaseModel):
    id: str
    name: str


class State1(BaseModel):
    id: str
    name: str


class SearchLocation(BaseModel):
    neighborhood: Neighborhood
    city: City1
    state: State1


class SellerAddress(BaseModel):
    city: City
    state: State
    country: Country
    search_location: SearchLocation
    id: int


class ValueStructItem1(BaseModel):
    number: float
    unit: str


class StructItem1(BaseModel):
    number: float
    unit: str


class Value1(BaseModel):
    id: Optional[str]
    name: Optional[str]
    struct: Optional[StructItem1]


class Attribute(BaseModel):
    id: str
    name: str
    value_id: Optional[str]
    value_name: Optional[str]
    value_struct: Optional[ValueStructItem1]
    values: List[Value1]
    attribute_group_id: str
    attribute_group_name: str


class Producto(BaseModel):
    id: str
    site_id: str
    title: str
    subtitle: Any
    seller_id: int
    category_id: str
    official_store_id: int
    price: int
    base_price: int
    original_price: Any
    currency_id: str
    initial_quantity: int
    available_quantity: int
    sold_quantity: int
    sale_terms: List[SaleTerm]
    buying_mode: str
    listing_type_id: str
    start_time: str
    stop_time: str
    condition: str
    permalink: str
    thumbnail_id: str
    thumbnail: str
    secure_thumbnail: str
    pictures: List[Picture]
    video_id: Any
    descriptions: List[Description]
    accepts_mercadopago: bool
    non_mercado_pago_payment_methods: List
    shipping: Shipping
    international_delivery_mode: str
    seller_address: SellerAddress
    seller_contact: Any
    location: Dict[str, Any]
    coverage_areas: List
    attributes: List[Attribute]
    warnings: List
    listing_source: str
    variations: List
    status: str
    sub_status: List
    tags: List[str]
    warranty: str
    catalog_product_id: str
    domain_id: str
    parent_item_id: Any
    differential_pricing: Any
    deal_ids: List[str]
    automatic_relist: bool
    date_created: str
    last_updated: str
    health: Any
    catalog_listing: bool
    channels: List[str]


