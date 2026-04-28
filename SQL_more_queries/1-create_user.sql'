-- İstifadəçi mövcud deyilsə, onu 'user_0d_1_pwd' şifrəsi ilə yaradır
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- İstifadəçiyə serverdəki bütün məlumat bazaları və cədvəllər üzərində tam səlahiyyət verir
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Dəyişikliklərin dərhal qüvvəyə minməsini təmin edir
FLUSH PRIVILEGES;
