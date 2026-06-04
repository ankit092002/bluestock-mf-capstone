-- =====================================
-- DROP TABLES IF EXIST
-- =====================================

DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS fact_performance;ṇṇṇ
DROP TABLE IF EXISTS fact_aum;

DROP TABLE IF EXISTS dim_fund;
DROP TABLE IF EXISTS dim_date;

-- =====================================
-- DIMENSION TABLE : FUND
-- =====================================

CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE NOT NULL,
    scheme_name TEXT NOT NULL,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_level TEXT
);

-- =====================================
-- DIMENSION TABLE : DATE
-- =====================================

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE UNIQUE NOT NULL,
    day INTEGER,
    month INTEGER,
    month_name TEXT,
    quarter INTEGER,
    year INTEGER,
    weekday TEXT
);

-- =====================================
-- FACT TABLE : NAV HISTORY
-- =====================================

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,

    nav REAL NOT NULL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- =====================================
-- FACT TABLE : INVESTOR TRANSACTIONS
-- =====================================

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,

    investor_id TEXT,

    transaction_type TEXT,

    amount REAL NOT NULL,

    state TEXT,

    kyc_status TEXT,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- =====================================
-- FACT TABLE : PERFORMANCE
-- =====================================

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,

    return_1m REAL,
    return_3m REAL,
    return_6m REAL,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,

    expense_ratio REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id)
);

-- =====================================
-- FACT TABLE : AUM
-- =====================================

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER NOT NULL,

    date_id INTEGER NOT NULL,

    aum REAL NOT NULL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);