

const redditstreamUser = process.env.DB_USER || 'nayeon';
const redditstreamPassword = process.env.DB_PASSWORD || 'watermelon';
const redditstreamDatabase = process.env.DB_DATABASE || 'redditstream';


db.createUser(
        {
            user: redditstreamUser,
            pwd: redditstreamPassword,
            roles: [
                {
                    role: "readWrite",
                    db: redditstreamDatabase
                }
            ]
        }
);