CREATE TABLE pokemon (
    poke_id serial primary key,
    dex_num int unique not null.
    poke_name  text
);

CREATE TABLE type_chart (
    type_id serial primary key,
    type_name text
);

CREATE TABLE assn_poke_type (
    assn_poke_type_id serial primary key,
    poke_id int references pokemon(poke_id),
    type_id int references type_chart(type_id),
    unique(poke_id, type_id)
);

CREATE TABLE assn_type_eff (
    assn_type_eff_id serial primary key,
    atk_type_id int references type_chart(type_id),
    def_type_id int references type_chart(type_id)
    eff_rate int,
    unique(atk_type_id, def_type_id)
);
