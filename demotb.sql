PGDMP     (    1        	        |            demodb    15.1    15.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                        1262    62508    demodb    DATABASE     y   CREATE DATABASE demodb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE demodb;
                postgres    false            �            1259    62513    demotb    TABLE     �   CREATE TABLE public.demotb (
    id integer NOT NULL,
    "left" integer,
    "right" integer,
    top integer,
    bottom integer
);
    DROP TABLE public.demotb;
       public         heap    postgres    false            �            1259    62512    demotb_id_seq    SEQUENCE     �   CREATE SEQUENCE public.demotb_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.demotb_id_seq;
       public          postgres    false    215                       0    0    demotb_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.demotb_id_seq OWNED BY public.demotb.id;
          public          postgres    false    214            h           2604    62516 	   demotb id    DEFAULT     f   ALTER TABLE ONLY public.demotb ALTER COLUMN id SET DEFAULT nextval('public.demotb_id_seq'::regclass);
 8   ALTER TABLE public.demotb ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �          0    62513    demotb 
   TABLE DATA           B   COPY public.demotb (id, "left", "right", top, bottom) FROM stdin;
    public          postgres    false    215   `
                  0    0    demotb_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.demotb_id_seq', 50, true);
          public          postgres    false    214            j           2606    62518    demotb demotb_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.demotb
    ADD CONSTRAINT demotb_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.demotb DROP CONSTRAINT demotb_pkey;
       public            postgres    false    215            �   �   x�mӱ�0E�Z�ŁE~��.��,p�+H>��3�ܽϸǵV��*���f]��ڪ�+����>��.���"�.ڊ���h+ڊ���ikښ��2ikښ6�&�	n�Cp�!8����B[h��L^�r���3��R���     