CREATE TABLE "Users" (
  "id" uuid4 UNIQUE PRIMARY KEY NOT NULL,
  "username" varchar(25) NOT NULL,
  "description" varchar(255),
  "role_id" serial NOT NULL,
  "created_at" timestamp NOT NULL,
  "phone_number" integer UNIQUE NOT NULL,
  "gender_id" serial NOT NULL,
  "city_id" serial NOT NULL,
  "rating" integer NOT NULL DEFAULT 30,
  "age" integer NOT NULL
);

CREATE TABLE "Roles" (
  "id" serial PRIMARY KEY,
  "name" varchar(25) NOT NULL,
  "description" varchar(255)
);

CREATE TABLE "Genders" (
  "id" serial PRIMARY KEY,
  "name" varchar(25) NOT NULL,
  "description" varchar(255)
);

CREATE TABLE "Cities" (
  "id" serial PRIMARY KEY,
  "name" varchar(25) NOT NULL
);

CREATE TABLE "Actions" (
  "id" uuid4 UNIQUE PRIMARY KEY NOT NULL,
  "from_id" uuid4 NOT NULL,
  "to_id" uuid4 NOT NULL,
  "type" serial NOT NULL,
  "occurred_at" timestamp NOT NULL
);

CREATE TABLE "Action_types" (
  "id" serial PRIMARY KEY,
  "name" varchar(25) NOT NULL,
  "description" varchar(255)
);

CREATE TABLE "User_images" (
  "id" uuid4 UNIQUE PRIMARY KEY NOT NULL,
  "user_id" uuid4 NOT NULL,
  "priority" integer NOT NULL DEFAULT 1
);

COMMENT ON COLUMN "Roles"."name" IS 'Name of the role';

COMMENT ON COLUMN "Roles"."description" IS 'Description of the role';

COMMENT ON COLUMN "Genders"."name" IS 'Name of the gender';

COMMENT ON COLUMN "Genders"."description" IS 'Description of the gender';

COMMENT ON COLUMN "Cities"."name" IS 'Name of the city';

ALTER TABLE "Roles" ADD FOREIGN KEY ("id") REFERENCES "Users" ("role_id");

ALTER TABLE "Genders" ADD FOREIGN KEY ("id") REFERENCES "Users" ("gender_id");

ALTER TABLE "Cities" ADD FOREIGN KEY ("id") REFERENCES "Users" ("city_id");

ALTER TABLE "Actions" ADD FOREIGN KEY ("from_id") REFERENCES "Users" ("id");

ALTER TABLE "Actions" ADD FOREIGN KEY ("to_id") REFERENCES "Users" ("id");

ALTER TABLE "User_images" ADD FOREIGN KEY ("user_id") REFERENCES "Users" ("id");

ALTER TABLE "Actions" ADD FOREIGN KEY ("type") REFERENCES "Action_types" ("id");
