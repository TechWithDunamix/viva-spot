from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "resturants" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted" BOOL NOT NULL DEFAULT False,
    "delivery" BOOL NOT NULL DEFAULT True,
    "zones" JSONB NOT NULL,
    "address_form_fields" JSONB NOT NULL,
    "pickups" BOOL NOT NULL DEFAULT False,
    "reservation" BOOL NOT NULL DEFAULT True,
    "minimum_guest" INT NOT NULL DEFAULT 0,
    "maximum_guest" INT NOT NULL DEFAULT 8,
    "allow_pre_order" INT NOT NULL DEFAULT 2,
    "maximu_time_in_advance" INT NOT NULL DEFAULT 8,
    "mimimum_time_in_advance" INT NOT NULL DEFAULT 8,
    "name" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(255),
    "country" VARCHAR(255),
    "timezone" VARCHAR(255),
    "state" VARCHAR(255),
    "postal_code" VARCHAR(255),
    "street_name" TEXT,
    "website" VARCHAR(255),
    "full_address" TEXT,
    "restricted" BOOL NOT NULL DEFAULT False,
    "confirmed" BOOL NOT NULL DEFAULT False
);
CREATE TABLE IF NOT EXISTS "users_base_account" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "deleted" BOOL NOT NULL DEFAULT False,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "hashed_password" TEXT NOT NULL,
    "account_type" VARCHAR(255) NOT NULL,
    CONSTRAINT "uid_users_base__email_caa316" UNIQUE ("email")
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
