import config

groups = [
    {
        'name': 'Crocca Blog',
        'difficulty': 'Easy - SQLi from first principles',
        'flavor': 'What are you gonna do? Dump the users table?',
        'db': config.db_setup['blog']
    },
    {
        'name': 'Crocca Videos',
        'difficulty': 'Beginner - Actually SQLi, not just SQL puzzles',
        'flavor': 'Yay! You might be able to get the password of the one guy who still rents videos...',
        'db': config.db_setup['video']
    },
    {
        'name': 'Crocca Bank',
        'difficulty': 'Intermediate - More realistic scenarios, but still with some help',
        'flavor': 'We\'re in the process of suing quoccabank for trademark infringement.',
        'db': config.db_setup['bank']
    },
    {
        'name': 'Crocca Flag',
        'difficulty': 'Advanced - Feedback is for n00bs',
        'flavor': 'Who cares about securing your money when you can secure your flags instead?',
        'db': config.db_setup['flag']
    },
    {
        'name': 'Crocca IRanOutOfScenarios',
        'difficulty': 'Extreme - Almost as hard as frontend design',
        'flavor': 'I couldn\'t think of anything more critical than a flag storage system.',
        'db': config.db_setup['scenario']
    }
]

levels = [
    # Sql challenges
    {
        'type': 'sql',
        'group': 0,
        'name': 'User 1',
        'spec': {
            'question': 'Find me the user whose id is 1.',
            'template': 'SELECT * FROM users WHERE id={q0}',
            'match': 'SELECT * FROM users WHERE id=1',
            'flag': 'FLAG{users_are_just_a_number}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sql',
        'group': 0,
        'name': 'Bobby',
        'spec': {
            'question': 'Find me the user with username bobby.',
            'template': 'SELECT * FROM users WHERE {q0}',
            'match': 'SELECT * FROM users WHERE username=\'bobby\'',
            'flag': 'FLAG{bobby_tables_is_coming_for_you}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sql',
        'group': 0,
        'name': 'ypfp',
        'spec': {
            'question': 'Find me only the password for the user with username ypfp.',
            'template': 'SELECT {q0} FROM users WHERE {q1}',
            'match': 'SELECT password FROM users WHERE username=\'ypfp\'',
            'flag': 'FLAG{very_secure_password}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sql',
        'group': 0,
        'name': 'Blogs 1',
        'spec': {
            'question': 'Find me all the blogs belonging to the user with id 1.',
            'template': 'SELECT * FROM {q0} WHERE {q1}',
            'match': 'SELECT * FROM blogs WHERE author_id=1',
            'flag': 'FLAG{ofc_its_a_blog_app}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sql',
        'group': 0,
        'name': 'Number 1',
        'spec': {
            'question': 'Dump the users table.',
            'template': '{q0}',
            'match': 'SELECT * FROM users',
            'flag': 'FLAG{bobby_tables_is_dumb}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sql',
        'group': 0,
        'name': 'Number 2',
        'spec': {
            'question': 'Dump the user and blog tables.',
            'template': '{q0} UNION {q1}',
            'match': 'SELECT * FROM users UNION SELECT * FROM blogs',
            'flag': 'FLAG{do_i_have_the_entire_db_yet?}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sql',
        'group': 0,
        'name': 'Hidden',
        'spec': {
            'question': 'Theres another table in here. List the names of all tables in the database.',
            'template': 'SELECT {q0} FROM {q1}',
            'match': 'SELECT table_name FROM information_schema.tables',
            'flag': 'FLAG{shoulda_done_this_first}',
            'error-control': 'full'
        }
    },

    # Easy SQLi Challenges
    {
        'type': 'sqli-easy',
        'group': 1,
        'name': 'Find-Me',
        'spec': {
            'question': 'This input lets me search for users based on their username. Can you make it show me all users?',
            'template': 'SELECT * FROM users WHERE username = \'{q0}\'',
            'show': {
                'q0': 'Username (e.g. admin)'
            },
            'match': 'SELECT * FROM users',
            'flag': 'FLAG{or_one_equals_one}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sqli-easy',
        'group': 1,
        'name': 'Video Search',
        'spec': {
            'question': 'This box lets me search for videos based on their title. Make it show all videos, usernames, and passwords.',
            'show': {
                'q0': 'Video Title'
            },
            'template': 'SELECT * FROM videos WHERE title LIKE \'%{q0}%\'',
            'match': 'SELECT * FROM videos UNION SELECT username, password FROM users',
            'flag': 'FLAG{dump_it_all!!!}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sqli-easy',
        'group': 1,
        'name': 'Postcode Search',
        'spec': {
            'question': 'This box lets me search for all rental peroids for users in a particular postcode. Make it show me payment information instead.',
            'show': {
                'q0': 'Postcode (e.g. 2000)'
            },
            'template': 'SELECT period FROM rentals WHERE user_id IN (SELECT id FROM users WHERE postcode=\'{q0}\')',
            'match': 'SELECT payment FROM rentals',
            'flag': 'FLAG{I_can_sql_inject!!!}',
            'error-control': 'full'
        }
    },
    {
        'type': 'sqli-easy',
        'group': 1,
        'name': 'Information',
        'spec': {
            'question': 'This box searches for postcodes based on username. Make it list all tables instead.',
            'show': {
                'q0': 'Username (e.g. admin)'
            },
            'template': 'SELECT postcode FROM users WHERE username=\'{q0}\'',
            'match': 'SELECT table_name FROM information_schema.tables',
            'flag': 'FLAG{I_keep_forgetting_to_do_this_first}',
            'error-control': 'full'
        }
    },

    # Medium SQLi Challenges
    {
        'type': 'sqli-medium',
        'group': 2,
        'name': 'Users ... again',
        'spec': {
            'question': 'Same deal. Box searches for users based on username. I want everyone.',
            'show': {
                'q0': 'Username (e.g. iamauser)'
            },
            'template': 'SELECT * FROM users WHERE username=\'{q0}\'',
            'match': 'SELECT * FROM users',
            'flag': 'FLAG{Im_a_strong_independant_hacker}',
            'error-control': 'error'
        }
    },
    {
        'type': 'sqli-medium',
        'group': 2,
        'name': 'Information II',
        'spec': {
            'question': 'This box searches for balance based on username. List me all the tables.',
            'show': {
                'q0': 'Username (e.g. iamauser)'
            },
            'template': 'SELECT balance FROM accounts INNER JOIN users ON accounts.user_id = users.id WHERE users.username=\'{q0}\'',
            'match': 'SELECT table_name FROM information_schema.tables',
            'flag': 'FLAG{I_remebered!_are_you_proud_of_me?}',
            'error-control': 'error'
        }
    },
    {
        'type': 'sqli-medium',
        'group': 2,
        'name': 'Moar Info!',
        'spec': {
            'question': 'This box searches for balance based on user id. List me the name of all the columns in the users table',
            'show': {
                'q0': 'User Id (e.g. 1)'
            },
            'template': 'SELECT balance FROM accounts WHERE user_id={q0}',
            'match': 'SELECT column_name FROM information_schema.columns WHERE table_name=\'users\'',
            'flag': 'FLAG{I_want_the_whole_schema_>:)}',
            'error-control': 'error',
        }
    },
    {
        'type': 'sqli-medium',
        'group': 2,
        'name': 'CreditCard',
        'spec': {
            'question': 'This box searches for the balances based on account name. I want a list all bank card numbers.',
            'show': {
                'q0': 'Account name (e.g. netbank)'
            },
            'template': 'SELECT balance FROM accounts WHERE name=\'{q0}\'',
            'match': 'SELECT card_number FROM cards',
            'flag': 'FLAG{in_credit_ble_..._sorry}',
            'error-control': 'error'
        }
    },

    # Hard SQLi Challenges
    {
        'type': 'sqli-hard',
        'group': 3,
        'name': 'Flag lookup',
        'spec': {
            'question': 'This box searches for score based on flag id. Show me a list of table names instead',
            'show': {
                'q0': 'Flag Id',
            },
            'template': 'SELECT score FROM flags WHERE id=\'{q0}\'',
            'match': 'SELECT table_name FROM information_schema.tables',
            'flag': 'FLAG{last_time_ill_ask_for_that}',
            'error-control': 'blind'
        }
    },
    {
        'type': 'sqli-hard',
        'group': 3,
        'name': 'Score lookup',
        'spec': {
            'question': 'This box searches for flags and scores based on flag id. Fetch usernames and passwords instead.',
            'show': {
                'q0': 'Flag Id'
            },
            'template': 'SELECT flag, score FROM flags WHERE id={q0}',
            'match': 'SELECT username, password FROM users',
            'flag': 'FLAG{assume_nothing}',
            'error-control': 'blind'
        }
    },
    {
        'type': 'sqli-hard',
        'group': 3,
        'name': 'Score finder',
        'spec': {
            'question': 'Give me a username and I\'ll give you their flags. What you want username and passwords? Nahhhh...',
            'show': {
                'q0': 'username'
            },
            'template': 'SELECT score, flag FROM solves INNER JOIN flags ON flags.id = solves.flag_id WHERE solves.user_id = (SELECT id FROM users WHERE username = \'{q0}\' LIMIT 1)',
            'match': 'SELECT username, password FROM users',
            'flag': 'FLAG{security_through_spaghetti}',
            'error-control': 'blind'
        }
    }

    # Extreme SQLi Challenges
]
