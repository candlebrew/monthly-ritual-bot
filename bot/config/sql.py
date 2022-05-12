# USER DATA ----------------------------
userDataTableSQL = '''CREATE TABLE IF NOT EXISTS user_data (
        uid BIGINT,
        theme TEXT DEFAULT 'ww',
        safe_pw BYTEA,
        unsafe_pw BYTEA,
        security_hold BOOL DEFAULT FALSE,
        men_len SMALLINT DEFAULT 4,
        total_len SMALLINT DEFAULT 28,
        men_to_ov_len SMALLINT DEFAULT 9,
        last_men_start TIMESTAMPTZ,
        next_men_start TIMESTAMPTZ,
        last_ov_start TIMESTAMPTZ,
        next_ov_start TIMESTAMPTZ,
        men_to_ov_lens INT[],
        men_lens INT[],
        total_lens INT[]
        );'''
## theme: pirate/ww/vamp/scifi/western/eldritch/custom/human
## next_men_start: last_men_start + men_len
## men_to_ov_len: last_men_start <> last_ov_start
## next_ov_start: last_men_start + men_to_ov_len

## PREFERENCES --------------------------
prefTableSQL = '''CREATE TABLE IF NOT EXISTS preferences (
        uid BIGINT,
        water_alert BOOL DEFAULT FALSE,
        water_min SMALLINT DEFAULT 0,
        water_hr SMALLINT DEFAULT 1,
        med_alert BOOL DEFAULT FALSE,
        med_frequency TEXT,
        med_time TIMESTAMPTZ,
        med_next_alert TIMESTAMPTZ,
        hrt_alert BOOL DEFAULT FALSE,
        hrt_frequency TEXT,
        hrt_time TIMESTAMPTZ,
        hrt_next_alert TIMESTAMPTZ
        );'''
## frequencies: daily/weekly/biweekly/monthly

## SYMPTOMS -----------------------------
symptomsTableSQL = '''CREATE TABLE IF NOT EXISTS symptoms (
        uid BIGINT,
        id SERIAL UNIQUE,
        time TIMESTAMPTZ,
        symptom TEXT,
        rating TEXT
        );'''

## ENCOUNTERS ---------------------------
encountersTableSQL = '''CREATE TABLE IF NOT EXISTS encounters (
        uid BIGINT,
        id SERIAL UNIQUE,
        start TIMESTAMPTZ,
        end TIMESTAMPTZ,
        length SMALLINT,
        abnormal BOOL DEFAULT FALSE,
        rating TEXT,
        type TEXT
        );'''

## TERMS --------------------------
defaultTermsTableSQL = '''CREATE TABLE IF NOT EXISTS default_terms (
        name TEXT,
        alias TEXT,
        type TEXT
        );'''

customTermsTableSQL = '''CREATE TABLE IF NOT EXISTS custom_terms (
        uid BIGINT,
        name TEXT,
        alias TEXT,
        type TEXT
        );'''
