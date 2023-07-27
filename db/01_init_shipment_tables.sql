CREATE TABLE IF NOT EXISTS public.shipment
(
    id                      serial           primary key,
    tracking_number         varchar          not null,
    carrier                 varchar          not null,
    sender_address_id       integer          not null,
    receiver_address_id     integer          not null,
    article_name            varchar          not null,
    article_quantity        varchar          not null,
    article_price           double precision not null,
    sku                     varchar          not null,
    status                  varchar          not null
);

CREATE TABLE IF NOT EXISTS public.address
(
    id                   serial           primary key,
    street               varchar          not null,
    house_no             varchar          not null,
    city                 varchar          not null,
    pin_code             varchar          not null,
    country              varchar          not null
);
