create database quan_ly_sv
CREATE TABLE `quan_ly_sv`.`sinh_vien` (
  `Mon_hoc` VARCHAR(45) NULL,
  `Ma_mon_hoc` VARCHAR(45) NULL,
  `Hoc_ki` VARCHAR(45) NULL,
  `Nam_hoc` VARCHAR(45) NULL,
  `Tin_chi` VARCHAR(45) NULL,
  `Ma_sv` INT NOT NULL,
  `Ten_sv` VARCHAR(45) NULL,
  `Gioi_tinh` VARCHAR(45) NULL,
  `Ngay_sinh` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `SDT` VARCHAR(45) NULL,
  `Noi_tam_tru` VARCHAR(45) NULL,
  `Que_quan` VARCHAR(45) NULL,
  PRIMARY KEY (`Ma_sv`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;