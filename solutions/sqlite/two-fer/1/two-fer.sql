--

UPDATE twofer
SET response = CASE
    WHEN input IS NULL OR trim(input) = ''
        THEN 'One for you, one for me.'
    ELSE 'One for ' || input || ', one for me.'
END;