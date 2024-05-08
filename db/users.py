class users:
    def get_user_by_user_email(self, user_email):
        query={'user_email':user_email}

        return self.users.find_one(query)

    def get_user_by_user_uuid(self, user_uuid):
        query={'user_uuid':user_uuid}

        return self.users.find_one(query)

    def get_users(self, limit, skip):
        users=[]
        cursor=self.users.find().skip(skip).limit(limit)
        
        for user in cursor:
            users.append(user)
            
        return users

    def get_user_addresses(self, user_uuid, limit, skip):
        addresses=[]

        query={
            "user_uuid": user_uuid
        }

        cursor=self.user_addresses.find(query).skip(skip).limit(limit)

        for address in cursor:
            addresses.append(address)

        return addresses

    def create_user(self, user_uuid, user_email, password_hash, group):
        document={
            "user_uuid": user_uuid,
            "user_email": user_email,
            "password_hash": password_hash,
            "group": group
        }

        self.users.insert_one(document)


