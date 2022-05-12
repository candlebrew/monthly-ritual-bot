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
