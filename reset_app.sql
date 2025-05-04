DROP TABLE IF EXISTS at_app_asset CASCADE;
DROP TABLE IF EXISTS at_app_department CASCADE;
DELETE FROM django_migrations WHERE app = 'at_app';